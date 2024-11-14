import random

from loguru import logger
from utils.gas_checker import check_gas
from utils.helpers import retry
from config import *
from .account import Account
from utils.sleeping import sleep



class Deployer(Account):
    def __init__(self, account_id: int, private_key: str, recipient: str) -> None:
        super().__init__(account_id=account_id, private_key=private_key, chain="base", recipient=recipient)

    @retry
    @check_gas
    async def deploy_token(self):
        logger.info(f"[{self.account_id}][{self.address}] Deploy contract")

        deployer = random.choice(deployers)
        logger.info(f"For [{self.account_id}][{self.address}] deployer {deployer.get('name')} ")
        contract = self.w3.eth.contract(
            abi=deployer.get("abi"),
            bytecode=deployer.get("bytecode")
        )

        rand = random.randint(1, 4)
        logger.info(f'Duplicate  deployment {rand} times')
        for i in range(rand):
            tx_data = await self.get_tx_data()

            transaction = await contract.constructor().build_transaction(
                tx_data
            )

            signed_txn = await self.sign(transaction)

            txn_hash = await self.send_raw_transaction(signed_txn)

            await self.wait_until_tx_finished(txn_hash.hex())

            await sleep(25, 60)

