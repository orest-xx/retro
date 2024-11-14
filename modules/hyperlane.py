import random

from loguru import logger
from utils.gas_checker import check_gas
from utils.helpers import retry
from utils.sleeping import sleep
from .account import Account
from config import HYPERLANE_TOKEN_CONTRACT, HYPERLANE_TOKEN_ABI, HYPERLANE_HFTOKEN_CONTRACT, HYPERLANE_HFTOKEN_ABI


class HyperlaneTokenBridge(Account):
    def __init__(self, account_id: int, private_key: str, chain: str, recipient: str) -> None:
        super().__init__(account_id=account_id, private_key=private_key, chain=chain, recipient=recipient)

        self.chain_ids = {
            "optimism": 10,
            "celo": 42220,
            "avalanche": 43114,
            "polygon zkevm": 1101,
            "binance smart chain": 56,
            "moonbeam": 1284,
            "gnosis": 100,
            "arbitrum": 42161,
            "polygon": 137,
            "base": 8453,
            "scroll": 534352,
            "ethereum": 1,
            "dogechain": 2000,
            "flare": 14,
            "zetachain": 7000,
            "redstone": 690,
            "sei": 1329,
            "molten": 360,
            "shibarium": 109,
            "everclear": 25327,
        }

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
            f"[{self.account_id}][{self.address}] Bridge Hyperlane Token Bridge – {self.chain.title()} -> " +
            f"{destination_chain.title()} | {amount} ETH"
        )

        contract = self.get_contract(HYPERLANE_TOKEN_CONTRACT[self.chain], HYPERLANE_TOKEN_ABI)

        fee = await contract.functions.quoteBridge(self.chain_ids[destination_chain], amount_wei).call()
        tx_data = await self.get_tx_data(amount_wei + fee)

        # const tx = await contract.bridgeETH(domain, amount, { value: amount.add(quote) });
        transaction = await contract.functions.bridgeETH(self.chain_ids[destination_chain], amount_wei). \
            build_transaction(tx_data)

        signed_txn = await self.sign(transaction)

        txn_hash = await self.send_raw_transaction(signed_txn)

        await self.wait_until_tx_finished(txn_hash.hex())

    @retry
    @check_gas
    async def bridge_hft(
            self,
            destination_chain: str,
            min_amount: float,
            max_amount: float,
            decimal: int,
            all_amount: bool,
            min_percent: int,
            max_percent: int
    ):

        logger.info(
            f"[{self.account_id}][{self.address}] Bridge Hyperlane HFT Bridge – {self.chain.title()} -> " +
            f"{destination_chain.title()} "
        )

        contract = self.get_contract(HYPERLANE_HFTOKEN_CONTRACT[self.chain], HYPERLANE_HFTOKEN_ABI)

        tokens_amount_mint = random.randint(2, 6)
        tokens_amount_bridge = random.randint(1, 2)
        mint_price = (await contract.functions.fee().call()) * tokens_amount_mint

        estimate_fee = await contract.functions.quoteBridge(
            self.chain_ids[destination_chain],
        ).call()

        token_balance = round((await contract.functions.balanceOf(self.address).call()) / 10 ** 18)

        if (token_balance == 0) or (token_balance < tokens_amount_bridge):

            logger.info(
                f"Mint {tokens_amount_mint} HMEKL on Merkly Hyperlane. Network: {self.chain.title()}." +
                f" Price for mint: {mint_price / 10 ** 18:.6f} ETH")
            tx_data = await self.get_tx_data(mint_price)
            transaction = await contract.functions.mint(
                self.address,
                tokens_amount_mint
            ).build_transaction(tx_data)

            signed_txn = await self.sign(transaction)

            txn_hash = await self.send_raw_transaction(signed_txn)

            await self.wait_until_tx_finished(txn_hash.hex())

            await sleep(5, 10)
        else:
            logger.info(
                f"Have enough HMEKL balance: {token_balance}. Network: {self.chain.title()}")

        logger.info(
            f"Bridge tokens on Merkly Hyperlane from {self.chain.title()} -> {destination_chain.title()}."
            f" Price for bridge: {(estimate_fee / 10 ** 18):.6f} ETH")
        tx_data = await self.get_tx_data(estimate_fee)

        transaction = await contract.functions.bridgeHFT(self.chain_ids[destination_chain],
                                                         int(tokens_amount_bridge * 10 ** 18)). \
            build_transaction(tx_data)

        signed_txn = await self.sign(transaction)

        txn_hash = await self.send_raw_transaction(signed_txn)

        await self.wait_until_tx_finished(txn_hash.hex())
