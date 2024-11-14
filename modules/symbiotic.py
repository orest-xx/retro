from typing import Dict

from loguru import logger
from config import CBETH_CONTRACT, wBETH_CONTRACT, SYMBIOTIC_CBETH_CONTRACT, SYMBIOTIC_ABI, SYMBIOTIC_wBETH_CONTRACT
from utils.gas_checker import check_gas
from utils.helpers import retry
from utils.sleeping import sleep
from .account import Account


class Symbiotic(Account):
    def __init__(self, account_id: int, private_key: str, recipient: str) -> None:
        super().__init__(account_id=account_id, private_key=private_key, chain="ethereum", recipient=recipient)

        self.contract = self.get_contract(SYMBIOTIC_CBETH_CONTRACT, SYMBIOTIC_ABI)

        self.contract_binance = self.get_contract(SYMBIOTIC_wBETH_CONTRACT, SYMBIOTIC_ABI)

    async def get_deposit_amount(self):
        cbeth_contract = self.get_contract(CBETH_CONTRACT)

        amount = await cbeth_contract.functions.balanceOf(self.address).call()

        return amount

    @retry
    @check_gas
    async def deposit(
            self,
            min_amount: float,
            max_amount: float,
            decimal: int,
            sleep_from: int,
            sleep_to: int,
            binance: bool,
            all_amount: bool,
            min_percent: int,
            max_percent: int
    ) -> None:
        if binance:
            wtoken = "ETH_wbETH"
        else:
            wtoken = "ETH_cbETH"

        amount_wei, amount, balance = await self.get_amount(
            wtoken,
            min_amount,
            max_amount,
            decimal,
            all_amount,
            min_percent,
            max_percent
        )

        logger.info(f"[{self.account_id}][{self.address}] Make deposit on Symbiotic | {amount} {wtoken}")

        tx_data = await self.get_tx_data()

        if binance:
            await self.approve(amount, wBETH_CONTRACT, SYMBIOTIC_wBETH_CONTRACT)

            await sleep(sleep_from, sleep_to)

            transaction = await self.contract_binance.functions.deposit(
                self.address,
                amount_wei
            ).build_transaction(tx_data)
        else:
            await self.approve(amount, CBETH_CONTRACT, SYMBIOTIC_CBETH_CONTRACT)

            await sleep(sleep_from, sleep_to)

            transaction = await self.contract.functions.deposit(
                self.address,
                amount_wei
            ).build_transaction(tx_data)

        signed_txn = await self.sign(transaction)

        txn_hash = await self.send_raw_transaction(signed_txn)

        await self.wait_until_tx_finished(txn_hash.hex())
