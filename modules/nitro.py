import aiohttp
from loguru import logger
from utils.gas_checker import check_gas
from utils.helpers import retry
from .account import Account


class Nitro(Account):
    def __init__(self, account_id: int, private_key: str, chain: str, recipient: str) -> None:
        super().__init__(account_id=account_id, private_key=private_key, chain=chain, recipient=recipient)

        self.chain_ids = {
            "ethereum": "1",
            "arbitrum": "42161",
            "optimism": "10",
            "zksync": "324",
            "scroll": "534352",
            "base": "8453",
            "linea": "59144",
        }

    async def get_quote(self, amount: int, destination_chain: str):
        url = "https://api-beta.pathfinder.routerprotocol.com/api/v2/quote"

        params = {
            "fromTokenAddress": "0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE",
            "toTokenAddress": "0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE",
            "amount": amount,
            "fromTokenChainId": self.chain_ids[self.chain],
            "toTokenChainId": self.chain_ids[destination_chain],
            "partnerId": 1
        }

        async with aiohttp.ClientSession() as session:
            response = await session.get(url=url, params=params)

            transaction_data = await response.json()

            return transaction_data

    async def build_transaction(self, params: dict):
        url = "https://api-beta.pathfinder.routerprotocol.com/api/v2/transaction"

        async with aiohttp.ClientSession() as session:
            response = await session.post(url=url, json=params)

            transaction_data = await response.json()

            return transaction_data

    @retry
    @check_gas
    async def bridge(
            self,
            destination_chain: str,
            min_amount: float,
            max_amount: float,
            decimal: int,
            all_amount: bool,
            min_percent: int,
            max_percent: int
    ):
        amount_wei, amount, balance = await self.get_amount(
            "ETH",
            min_amount,
            max_amount,
            decimal,
            all_amount,
            min_percent,
            max_percent
        )

        logger.info(
            f"[{self.account_id}][{self.address}] Bridge Nitro – {self.chain.title()} -> " +
            f"{destination_chain.title()} | {amount} ETH"
        )

        quote = await self.get_quote(amount_wei, destination_chain)
        quote.update({"senderAddress": self.address, "receiverAddress": self.address})

        transaction_data = await self.build_transaction(quote)

        tx_data = await self.get_tx_data()
        tx_data.update(
            {
                "from": self.w3.to_checksum_address(transaction_data["txn"]["from"]),
                "to": self.w3.to_checksum_address(transaction_data["txn"]["to"]),
                "value": int(transaction_data["txn"]["value"], 16),
                "data": transaction_data["txn"]["data"],
            }
        )

        signed_txn = await self.sign(tx_data)

        txn_hash = await self.send_raw_transaction(signed_txn)

        await self.wait_until_tx_finished(txn_hash.hex())



# {
        #     "chainId": 534352,
        #     "data": "0xf452ed4d0000000000000000000000000000000000000000000000000000000000000001000000000000000000000000000000000000000000000000002386f26fc100000000000000000000000000000000000000000000000000000022a3fb2e455295000000000000000000000000eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee0000000000000000000000001bcc47183112f47d7d999501c3b620a1ccf3f3d13834353300000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000000000001400000000000000000000000000000000000000000000000000000000000000014eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee00000000000000000000000000000000000000000000000000000000000000000000000000000000000000141bcc47183112f47d7d999501c3b620a1ccf3f3d1000000000000000000000000",
        #     "from": "0x1bcc47183112f47d7d999501c3b620a1ccf3f3d1",
        #     "gas": "0x1865a",
        #     "gasPrice": "0x2160ec00",
        #     "nonce": "0x42",
        #     "to": "0x01b4ce0d48ce91eb6bcaf5db33870c65d641b894",
        #     "value": "0x2386f26fc10000"
        # }

        # {
        #     "chainId": 8453,
        #     "data": "0xf452ed4d000000000000000000000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000000470de4df8200000000000000000000000000000000000000000000000000000045a0e3381268f5000000000000000000000000eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee0000000000000000000000001bcc47183112f47d7d999501c3b620a1ccf3f3d13533343335320000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000000000001400000000000000000000000000000000000000000000000000000000000000014eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee00000000000000000000000000000000000000000000000000000000000000000000000000000000000000141bcc47183112f47d7d999501c3b620a1ccf3f3d1000000000000000000000000",
        #     "from": "0x1bcc47183112f47d7d999501c3b620a1ccf3f3d1",
        #     "gas": "0x15f2a",
        #     "gasPrice": "0xf116c0",
        #     "nonce": "0x74",
        #     "to": "0x0fa205c0446cd9eedcc7538c9e24bc55ad08207f",
        #     "value": "0x470de4df820000"
        # }


        # {
        #     "func": "iDeposit",
        #     "params": [
        #         [
        #             1,
        #             10000000000000000,
        #             9750448416576149,
        #             "0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE",
        #             "0x1bcC47183112f47d7D999501C3b620a1CcF3F3d1",
        #             "3834353300000000000000000000000000000000000000000000000000000000"
        #         ],
        #         "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee",
        #         "1bcc47183112f47d7d999501c3b620a1ccf3f3d1"
        #     ]
        # }