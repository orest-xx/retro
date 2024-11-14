---
Current repo is only for a learning purpose, review and test before use!

Interact with Scroll, Symbiotic, Hyperlane, Nitro, Orbiter

Repo is based on open source scroll soft 

Main goal to automate interactions with EVM compatible chains and protocols 
on EVM and/or L2 layers for Ethereum.

Using this repo you can bridge ETH and lend it to different protocols
   - Interact with cross-chain techs like L0, Hyperlane, Nitro, Orbiter 
   - Interact with Symbiotic liquid staking/restaking ETH protocol
   - Interact with Scroll ecosystem (Aave, Layerbank and several DEXes)
     - Deploy simple smart contracts
     - Deploy and mint your NFTs

---
<h3> How to </h3>
you need python 3.10 version (https://www.python.org/downloads/ )

```
git clone <current repo>

cd retro

pip install -r requirements.txt
# or (depends on python and pip versions)
pip3 install -r requirements.txt

# edit main method in main.py to configure which module to run
python main.py
or 
python3 main.py
```

1) To configure please edit next:
   - settings.py 
   - modules_settings.py
   - config.py 
   - accounts.txt (specify your private keys (be carefully of loosing your private keys))
   - rpc.json
---


