import asyncio
import random

from modules import *


async def deposit_scroll(account_id, key, recipient):
    """
    Deposit from official bridge
    ______________________________________________________
    all_amount - bridge from min_percent to max_percent
    """

    min_amount = 0.0002
    max_amount = 0.00044
    decimal = 4

    all_amount = False

    min_percent = 1
    max_percent = 1

    scroll = Scroll(account_id, key, "ethereum", recipient)
    await scroll.deposit(min_amount, max_amount, decimal, all_amount, min_percent, max_percent)


async def withdraw_scroll(account_id, key, recipient):
    """
    Withdraw from official bridge
    ______________________________________________________
    all_amount - withdraw from min_percent to max_percent
    """

    min_amount = 0.0012
    max_amount = 0.0012
    decimal = 4

    all_amount = True

    min_percent = 10
    max_percent = 10

    scroll = Scroll(account_id, key, "scroll", recipient)
    await scroll.withdraw(min_amount, max_amount, decimal, all_amount, min_percent, max_percent)


async def bridge_orbiter(account_id, key, recipient):
    """
    Bridge ETH using orbiter
    ______________________________________________________
    from_chain – ethereum, base, polygon_zkevm, arbitrum, optimism, zksync, scroll | Select one
    to_chain – ethereum, base, polygon_zkevm, arbitrum, optimism, zksync, scroll | Select one
    """

    from_chain = "scroll"
    to_chain = "base"

    min_amount = 0.005
    max_amount = 0.0051
    decimal = 4

    all_amount = False

    min_percent = 5
    max_percent = 10

    orbiter = Orbiter(account_id=account_id, private_key=key, chain=from_chain, recipient=recipient)
    await orbiter.bridge(to_chain, min_amount, max_amount, decimal, all_amount, min_percent, max_percent)


async def bridge_layerswap(account_id, key, recipient):
    """
    Bridge from Layerswap
    ______________________________________________________
    from_chain - Choose any chain: ethereum, arbitrum, optimism, avalanche, polygon, base, scroll
    to_chain - Choose any chain: ethereum, arbitrum, optimism, avalanche, polygon, base, scroll

    make_withdraw - True, if need withdraw after deposit

    all_amount - deposit from min_percent to max_percent
    """

    from_chain = "zksync"
    to_chain = "scroll"

    min_amount = 0.003
    max_amount = 0.004

    decimal = 5

    all_amount = True

    min_percent = 5
    max_percent = 5

    layerswap = LayerSwap(account_id=account_id, private_key=key, chain=from_chain, recipient=recipient)
    await layerswap.bridge(
        from_chain, to_chain, min_amount, max_amount, decimal, all_amount, min_percent, max_percent
    )


async def bridge_nitro(account_id, key, recipient):
    """
    Bridge from nitro
    ______________________________________________________
    from_chain – ethereum, arbitrum, optimism, zksync, scroll, base, linea | Select one
    to_chain – ethereum, arbitrum, optimism, zksync, scroll, base, linea | Select one
    """

    from_chain = "zksync"
    to_chain = "base"

    min_amount = 0.0014
    max_amount = 0.0015
    decimal = 4

    all_amount = True

    min_percent = 90
    max_percent = 90

    nitro = Nitro(account_id=account_id, private_key=key, chain=from_chain, recipient=recipient)
    await nitro.bridge(to_chain, min_amount, max_amount, decimal, all_amount, min_percent, max_percent)


async def bridge_nitro_in(account_id, key, recipient):
    """
    Bridge from nitro
    ______________________________________________________
    from_chain – ethereum, arbitrum, optimism, zksync, scroll, base, linea | Select one
    to_chain – ethereum, arbitrum, optimism, zksync, scroll, base, linea | Select one
    """

    from_chain = "base"
    to_chain = "scroll"

    min_amount = 0.0007
    max_amount = 0.0012
    decimal = 4

    all_amount = True

    min_percent = 90
    max_percent = 90

    nitro = Nitro(account_id=account_id, private_key=key, chain=from_chain, recipient=recipient)
    await nitro.bridge(to_chain, min_amount, max_amount, decimal, all_amount, min_percent, max_percent)

async def bridge_nitro_in2(account_id, key, recipient):
    """
    Bridge from nitro
    ______________________________________________________
    from_chain – ethereum, arbitrum, optimism, zksync, scroll, base, linea | Select one
    to_chain – ethereum, arbitrum, optimism, zksync, scroll, base, linea | Select one
    """

    from_chain = "optimism"
    to_chain = "base"

    min_amount = 0.0014
    max_amount = 0.0015
    decimal = 4

    all_amount = True

    min_percent = 97
    max_percent = 98

    nitro = Nitro(account_id=account_id, private_key=key, chain=from_chain, recipient=recipient)
    await nitro.bridge(to_chain, min_amount, max_amount, decimal, all_amount, min_percent, max_percent)



async def bridge_nitro_out(account_id, key, recipient):
    """
    Bridge from nitro
    ______________________________________________________
    from_chain – ethereum, arbitrum, optimism, zksync, scroll, base, linea | Select one
    to_chain – ethereum, arbitrum, optimism, zksync, scroll, base, linea | Select one
    """

    from_chain = "scroll"
    to_chain = "base"

    min_amount = 0.0021
    max_amount = 0.0023
    decimal = 4

    all_amount = True

    min_percent = 95
    max_percent = 95

    nitro = Nitro(account_id=account_id, private_key=key, chain=from_chain, recipient=recipient)
    await nitro.bridge(to_chain, min_amount, max_amount, decimal, all_amount, min_percent, max_percent)


async def bridge_hyperlane_in(account_id, key, recipient):
    """
    Bridge using hyperlane merkly eth
    ______________________________________________________
    from_chain – ethereum, arbitrum, optimism, zksync, scroll, base, linea | Select one
    to_chain – ethereum, arbitrum, optimism, zksync, scroll, base, linea | Select one
    """

    from_chain = "base"
    to_chain = "optimism"

    min_amount = 0.001
    max_amount = 0.001
    decimal = 4

    all_amount = True

    min_percent = 99
    max_percent = 99

    hyperlane = HyperlaneTokenBridge(account_id=account_id, private_key=key, chain=from_chain, recipient=recipient)
    await hyperlane.bridge(to_chain, min_amount, max_amount, decimal, all_amount, min_percent, max_percent)


async def bridge_hyperlane_out(account_id, key, recipient):
    """
    Bridge using hyperlane merkly eth
    ______________________________________________________
    from_chain – ethereum, arbitrum, optimism, zksync, scroll, base, linea | Select one
    to_chain – ethereum, arbitrum, optimism, zksync, scroll, base, linea | Select one
    """

    from_chain = "scroll"
    to_chain = random.choice(["base", "base"])

    min_amount = 0.001
    max_amount = 0.001
    decimal = 4

    all_amount = True

    min_percent = 90
    max_percent = 90

    hyperlane = HyperlaneTokenBridge(account_id=account_id, private_key=key, chain=from_chain, recipient=recipient)
    await hyperlane.bridge(to_chain, min_amount, max_amount, decimal, all_amount, min_percent, max_percent)


async def bridge_hyperlane(account_id, key, recipient):
    """
    Bridge using hyperlane merkly eth
    ______________________________________________________
    from_chain – ethereum, arbitrum, optimism, zksync, scroll, base, linea | Select one
    to_chain – ethereum, arbitrum, optimism, zksync, scroll, base, linea | Select one
    """

    from_chain = "optimism"
    to_chain = random.choice(["arbitrum", "arbitrum"])

    min_amount = 0.001
    max_amount = 0.001
    decimal = 4

    all_amount = True

    min_percent = 99
    max_percent = 99

    hyperlane = HyperlaneTokenBridge(account_id=account_id, private_key=key, chain=from_chain, recipient=recipient)
    await hyperlane.bridge(to_chain, min_amount, max_amount, decimal, all_amount, min_percent, max_percent)



async def bridge_hft_hyperlane_base(account_id, key, recipient):
    """
    Mint and bridge hft (non value token) using hyperlane merkly
    ______________________________________________________
    from_chain – ethereum, arbitrum, optimism, zksync, scroll, base, linea | Select one
    to_chain – ethereum, arbitrum, optimism, zksync, scroll, base, linea | Select one
    """

    from_chain = "base"
    to_chain = random.choice(["everclear", "everclear", "moonbeam", "moonbeam", "celo"])
    #base - celo(0.5),fuse(0.5),moonbeam(0.5),gnosis(0.5),polygon(0.5),zora(0.5),zeta(0.5),sei(0.5),zircuit(0.5),everclear(0.4),shibarium(0.5),flare(0.5),dogechain(0.5),
    #scroll - celo(0.5),fuse(0.5),moonbeam(0.5),polygon(0.5),zora(0.5),zeta(0.5),sei(0.5),zircuit(0.5),everclear(0.4),shibarium(0.5),flare(0.5),dogechain(0.5),

    min_amount = 0.001
    max_amount = 0.001
    decimal = 4

    all_amount = True

    min_percent = 99
    max_percent = 99

    hyperlane = HyperlaneTokenBridge(account_id=account_id, private_key=key, chain=from_chain, recipient=recipient)
    await hyperlane.bridge_hft(to_chain, min_amount, max_amount, decimal, all_amount, min_percent, max_percent)

async def bridge_hft_hyperlane_scroll(account_id, key, recipient):
    """
    Mint and bridge hft (non value token) using hyperlane merkly
    ______________________________________________________
    from_chain – ethereum, arbitrum, optimism, zksync, scroll, base, linea | Select one
    to_chain – ethereum, arbitrum, optimism, zksync, scroll, base, linea | Select one
    """

    from_chain = "scroll"
    to_chain = random.choice(["everclear", "everclear"])
    #base - celo(0.5),fuse(0.5),moonbeam(0.5),gnosis(0.5),polygon(0.5),zora(0.5),zeta(0.5),sei(0.5),zircuit(0.5),everclear(0.4),shibarium(0.5),flare(0.5),dogechain(0.5),
    #scroll - celo(0.5),fuse(0.5),moonbeam(0.5),polygon(0.5),zora(0.5),zeta(0.5),sei(0.5),zircuit(0.5),everclear(0.4),shibarium(0.5),flare(0.5),dogechain(0.5),

    min_amount = 0.001
    max_amount = 0.001
    decimal = 4

    all_amount = True

    min_percent = 99
    max_percent = 99

    hyperlane = HyperlaneTokenBridge(account_id=account_id, private_key=key, chain=from_chain, recipient=recipient)
    await hyperlane.bridge_hft(to_chain, min_amount, max_amount, decimal, all_amount, min_percent, max_percent)

async def wrap_eth(account_id, key, recipient):
    """
    Wrap ETH
    ______________________________________________________
    all_amount - wrap from min_percent to max_percent
    """

    min_amount = 0.001
    max_amount = 0.002
    decimal = 4

    all_amount = True

    min_percent = 50
    max_percent = 80

    scroll = Scroll(account_id, key, "scroll", recipient)
    await scroll.wrap_eth(min_amount, max_amount, decimal, all_amount, min_percent, max_percent)


async def unwrap_eth(account_id, key, recipient):
    """
    Unwrap ETH
    ______________________________________________________
    all_amount - unwrap from min_percent to max_percent
    """

    min_amount = 0.001
    max_amount = 0.002
    decimal = 4

    all_amount = True

    min_percent = 100
    max_percent = 100

    scroll = Scroll(account_id, key, "scroll", recipient)
    await scroll.unwrap_eth(min_amount, max_amount, decimal, all_amount, min_percent, max_percent)


async def swap_skydrome(account_id, key, recipient):
    """
    Make swap on Skydrome
    ______________________________________________________
    from_token – Choose SOURCE token ETH, USDC | Select one
    to_token – Choose DESTINATION token ETH, USDC | Select one

    Disclaimer - You can swap only ETH to any token or any token to ETH!
    ______________________________________________________
    all_amount - swap from min_percent to max_percent
    """

    from_token = "ETH"
    to_token = "USDC"

    min_amount = 0.0001
    max_amount = 0.0002
    decimal = 6
    slippage = 1

    all_amount = True

    min_percent = 10
    max_percent = 15

    skydrome = Skydrome(account_id, key, recipient)
    await skydrome.swap(
        from_token, to_token, min_amount, max_amount, decimal, slippage, all_amount, min_percent, max_percent
    )


async def swap_zebra(account_id, key, recipient):
    """
    Make swap on Zebra
    ______________________________________________________
    from_token – Choose SOURCE token ETH, USDC | Select one
    to_token – Choose DESTINATION token ETH, USDC | Select one

    Disclaimer - You can swap only ETH to any token or any token to ETH!
    ______________________________________________________
    all_amount - swap from min_percent to max_percent
    """

    from_token = "ETH"
    to_token = "USDC"

    min_amount = 0.0001
    max_amount = 0.0002
    decimal = 6
    slippage = 1

    all_amount = True

    min_percent = 10
    max_percent = 15

    zebra = Zebra(account_id, key, recipient)
    await zebra.swap(
        from_token, to_token, min_amount, max_amount, decimal, slippage, all_amount, min_percent, max_percent
    )


async def swap_syncswap(account_id, key, recipient):
    """
    Make swap on SyncSwap

    from_token – Choose SOURCE token ETH, USDC | Select one
    to_token – Choose DESTINATION token ETH, USDC | Select one

    Disclaimer – Don't use stable coin in from and to token | from_token USDC to_token USDT DON'T WORK!!!
    ______________________________________________________
    all_amount - swap from min_percent to max_percent
    """

    from_token = "USDC"
    to_token = "ETH"

    min_amount = 1
    max_amount = 2
    decimal = 6
    slippage = 1

    all_amount = True

    min_percent = 100
    max_percent = 100

    syncswap = SyncSwap(account_id, key, recipient)
    await syncswap.swap(
        from_token, to_token, min_amount, max_amount, decimal, slippage, all_amount, min_percent, max_percent
    )


async def swap_xyswap(account_id, key, recipient):
    """
    Make swap on XYSwap
    ______________________________________________________
    from_token – Choose SOURCE token ETH, WETH, USDC | Select one
    to_token – Choose DESTINATION token ETH, WETH, USDC | Select one

    Disclaimer - If you use True for use_fee, you support me 1% of the transaction amount
    ______________________________________________________
    all_amount - swap from min_percent to max_percent
    """

    from_token = "ETH"
    to_token = "ETH_cbETH" #coinbase
    to_token = "ETH_wbETH" #binance

    min_amount = 0.0005
    max_amount = 0.0011
    decimal = 6
    slippage = 1

    all_amount = False

    min_percent = 100
    max_percent = 100

    xyswap = XYSwap(account_id, key, recipient)
    await xyswap.swap(
        from_token, to_token, min_amount, max_amount, decimal, slippage, all_amount, min_percent, max_percent
    )


async def swap_xyswap_beth(account_id, key, recipient):
    """
    Make swap on XYSwap
    ______________________________________________________
    from_token – Choose SOURCE token ETH, WETH, USDC | Select one
    to_token – Choose DESTINATION token ETH, WETH, USDC | Select one

    Disclaimer - If you use True for use_fee, you support me 1% of the transaction amount
    ______________________________________________________
    all_amount - swap from min_percent to max_percent
    """

    from_token = "ETH"
    # to_token = "ETH_cbETH" #coinbase
    to_token = "ETH_wbETH" #binance

    min_amount = 0.0001
    max_amount = 0.0004
    decimal = 6
    slippage = 1

    all_amount = False

    min_percent = 100
    max_percent = 100

    xyswap = XYSwap(account_id, key, recipient)
    await xyswap.swap(
        from_token, to_token, min_amount, max_amount, decimal, slippage, all_amount, min_percent, max_percent
    )

async def swap_xyswap_cbeth(account_id, key, recipient):
    """
    Make swap on XYSwap
    ______________________________________________________
    from_token – Choose SOURCE token ETH, WETH, USDC | Select one
    to_token – Choose DESTINATION token ETH, WETH, USDC | Select one

    Disclaimer - If you use True for use_fee, you support me 1% of the transaction amount
    ______________________________________________________
    all_amount - swap from min_percent to max_percent
    """

    from_token = "ETH"
    to_token = "ETH_cbETH" #coinbase
    # to_token = "ETH_wbETH" #binance

    min_amount = 0.0002
    max_amount = 0.0005
    decimal = 6
    slippage = 1

    all_amount = False

    min_percent = 100
    max_percent = 100

    xyswap = XYSwap(account_id, key, recipient)
    await xyswap.swap(
        from_token, to_token, min_amount, max_amount, decimal, slippage, all_amount, min_percent, max_percent
    )


async def deposit_layerbank(account_id, key, recipient):
    """
    Make deposit on LayerBank
    ______________________________________________________
    make_withdraw - True, if need withdraw after deposit

    all_amount - deposit from min_percent to max_percent
    """
    min_amount = 0.0001
    max_amount = 0.0002
    decimal = 5

    sleep_from = 5
    sleep_to = 24

    make_withdraw = False

    all_amount = True

    min_percent = 92
    max_percent = 96

    layerbank = LayerBank(account_id, key, recipient)
    await layerbank.deposit(
        min_amount, max_amount, decimal, sleep_from, sleep_to, make_withdraw, all_amount, min_percent, max_percent
    )


async def deposit_aave(account_id, key, recipient):
    """
    Make deposit on Aave
    ______________________________________________________
    make_withdraw - True, if need withdraw after deposit

    all_amount - deposit from min_percent to max_percent
    """
    min_amount = 0.1
    max_amount = 0.102
    decimal = 5

    sleep_from = 15
    sleep_to = 44

    make_withdraw = False

    all_amount = True

    min_percent = 93
    max_percent = 96

    aave = Aave(account_id, key, recipient)
    await aave.deposit(
        min_amount, max_amount, decimal, sleep_from, sleep_to, make_withdraw, all_amount, min_percent, max_percent
    )


async def deposit_symbiotic_beth(account_id, key, recipient):
    """
    Make deposit on Aave
    ______________________________________________________
    make_withdraw - True, if need withdraw after deposit

    all_amount - deposit from min_percent to max_percent
    """
    min_amount = 0.1
    max_amount = 0.102
    decimal = 5

    sleep_from = 35
    sleep_to = 64

    binance = True

    all_amount = True

    min_percent = 100
    max_percent = 100

    symbiotic = Symbiotic(account_id, key, recipient)
    await symbiotic.deposit(
        min_amount, max_amount, decimal, sleep_from, sleep_to, binance, all_amount, min_percent, max_percent
    )

async def deposit_symbiotic_cbeth(account_id, key, recipient):
    """
    Make deposit on Aave
    ______________________________________________________
    make_withdraw - True, if need withdraw after deposit

    all_amount - deposit from min_percent to max_percent
    """
    min_amount = 0.1
    max_amount = 0.102
    decimal = 5

    sleep_from = 35
    sleep_to = 64

    binance = False

    all_amount = True

    min_percent = 100
    max_percent = 100

    symbiotic = Symbiotic(account_id, key, recipient)
    await symbiotic.deposit(
        min_amount, max_amount, decimal, sleep_from, sleep_to, binance, all_amount, min_percent, max_percent
    )


async def mint_l2pass(account_id, key, recipient):
    """
    Mint L2Pass NFT
    """

    contract = "0x0000049f63ef0d60abe49fdd8bebfa5a68822222"

    l2pass = L2Pass(account_id, key, recipient)
    await l2pass.mint(contract)


async def mint_nft(account_id, key, recipient):
    """
    Mint NFT on NFTS2ME
    ______________________________________________________
    contracts - list NFT contract addresses
    """

    contracts = [""]

    minter = Minter(account_id, key, recipient)
    await minter.mint_nft(contracts)


async def send_message(account_id, key, recipient):
    """
    Send message with L2Telegraph
    ______________________________________________________
    chain - select need chain to send message, you can specify several, one will be selected randomly

    availiable chaines: bsc, optimism, avalanche, arbitrum, polygon, linea, moonbeam, kava, telos, klaytn, gnosis, moonriver
    """
    use_chain = ["gnosis", "moonriver"]

    l2telegraph = L2Telegraph(account_id, key, recipient)
    await l2telegraph.send_message(use_chain)


async def bridge_nft(account_id, key, recipient):
    """
    Make mint NFT and bridge NFT on L2Telegraph
    ______________________________________________________
    chain - select need chain to send message, you can specify several, one will be selected randomly

    availiable chaines: bsc, optimism, avalanche, arbitrum, polygon, linea, moonbeam, kava, telos, klaytn, gnosis, moonriver
    """
    use_chain = ["gnosis", "moonriver"]

    sleep_from = 5
    sleep_to = 20

    l2telegraph = L2Telegraph(account_id, key, recipient)
    await l2telegraph.bridge(use_chain, sleep_from, sleep_to)


async def make_transfer(_id, key, recipient):
    """
    Transfer ETH
    """

    min_amount = 0.0001
    max_amount = 0.0002
    decimal = 5

    all_amount = True

    min_percent = 10
    max_percent = 10

    transfer = Transfer(_id, key, recipient)
    await transfer.transfer(min_amount, max_amount, decimal, all_amount, min_percent, max_percent)


async def swap_tokens(account_id, key, recipient):
    """
    SwapTokens module: Automatically swap tokens to ETH
    ______________________________________________________
    use_dex - Choose any dex: syncswap, skydrome, zebra, xyswap
    """

    use_dex = [
        "syncswap", "skydrome", "zebra"
    ]

    use_tokens = ["USDC"]

    sleep_from = 21
    sleep_to = 65

    slippage = 0.1

    min_percent = 100
    max_percent = 100

    swap_tokens = SwapTokens(account_id, key, recipient)
    await swap_tokens.swap(use_dex, use_tokens, sleep_from, sleep_to, slippage, min_percent, max_percent)


async def swap_multiswap(account_id, key, recipient):
    """
    Multi-Swap module: Automatically performs the specified number of swaps in one of the dexes.
    ______________________________________________________
    use_dex - Choose any dex: syncswap, skydrome, zebra, xyswap
    quantity_swap - Quantity swaps
    ______________________________________________________
    If back_swap is True, then, if USDC remains, it will be swapped into ETH.
    """

    use_dex = ["syncswap", "skydrome"] #, "zebra"

    min_swap = 1
    max_swap = 2

    sleep_from = 23
    sleep_to = 57

    slippage = 0.1

    back_swap = True

    min_percent = 25
    max_percent = 34

    multi = Multiswap(account_id, key, recipient)
    await multi.swap(
        use_dex, sleep_from, sleep_to, min_swap, max_swap, slippage, back_swap, min_percent, max_percent
    )


async def custom_routes(account_id, key, recipient):
    """
    BRIDGE:
        – deposit_scroll
        – withdraw_scroll
        – bridge_orbiter
        – bridge_layerswap
        – bridge_nitro
    WRAP:
        – wrap_eth
        – unwrap_eth
    DEX:
        – swap_skydrome
        – swap_syncswap
        – swap_zebra
    LIQUIDITY:
    LANDING:
        – depost_layerbank
        – withdraw_layerbank
        – deposit_aave
        – withdraw_aave
    NFT/DOMAIN:
        – create_omnisea
        – mint_nft
        – mint_l2pass
    ANOTHER:
        – swap_multiswap
        – swap_tokens
        – send_mail (Dmail)
        – create_safe
        – deploy_contract
    ______________________________________________________
    Disclaimer - You can add modules to [] to select random ones,
    example [module_1, module_2, [module_3, module_4], module 5]
    The script will start with module 1, 2, 5 and select a random one from module 3 and 4

    You can also specify None in [], and if None is selected by random, this module will be skipped

    You can also specify () to perform the desired action a certain number of times
    example (send_mail, 1, 10) run this module 1 to 10 times
    """

    use_modules = [
        # wrap_eth, unwrap_eth, swap_skydrome, [swap_xyswap, swap_syncswap]
        # [swap_zebra, swap_skydrome], [swap_xyswap, swap_syncswap], [deposit_aave, deposit_layerbank]
        # swap_multiswap, [deposit_aave, deposit_layerbank]
        # withdraw_layerbank, swap_tokens
        # bridge_nitro_in, bridge_nitro_in2,
        # bridge_nitro,

        # bridge_hft_hyperlane_base, bridge_hft_hyperlane_scroll, [bridge_hft_hyperlane_base, None]
        # withdraw_layerbank, #,
        # withdraw_aave, #,
        # bridge_hyperlane_out
        bridge_nitro_out

        # bridge_nitro_in,
        # withdraw_layerbank
        # withdraw_aave
        # bridge_hyperlane

        # swap_xyswap_beth,
        # deposit_symbiotic_beth

        # swap_xyswap_cbeth,
        # deposit_symbiotic_cbeth

        # deploy_contract, [deploy_contract, None], [deploy_contract, None], deploy_contract, [deploy_contract, None]
        # pump_claim

        # swap_tokens
        # deposit_layerbank
        # bridge_nitro
        # bridge_nitro_out

        # swap_tokens
        # deposit_scroll, swap_multiswap, [deposit_aave, deposit_layerbank], [deposit_aave, None]

        # bridge_nitro_in, swap_multiswap, [deposit_aave, deposit_layerbank],
        # wrap_eth, unwrap_eth, [deposit_aave, None], swap_tokens, bridge_hyperlane_out,
        # bridge_nitro, bridge_nitro_out,
        # bridge_hyperlane_in, bridge_hyperlane

        # withdraw_layerbank,
        # withdraw_aave,
        # unwrap_eth
        # wrap_eth, unwrap_eth, [deposit_aave, None], [deposit_layerbank, None], swap_tokens, bridge_hyperlane_out

        # [swap_xyswap, swap_syncswap]
        # bridge_nitro_out #, bridge_nitro_out
        # [create_omnisea, mint_zerius, None],
        # (create_omnisea, 1, 3),
    ]

    sleep_from = 30
    sleep_to = 80

    random_module = False

    routes = Routes(account_id, key, recipient)
    await routes.start(use_modules, sleep_from, sleep_to, random_module)


#########################################
########### NO NEED TO CHANGE ###########
#########################################

async def withdraw_layerbank(account_id, key, recipient):
    layerbank = LayerBank(account_id, key, recipient)
    await layerbank.withdraw()


async def withdraw_aave(account_id, key, recipient):
    aave = Aave(account_id, key, recipient)
    await aave.withdraw()

async def pump_claim(account_id, key, recipient):
    module = ScrollPump(account_id, key, recipient)
    await module.claim()

async def send_mail(account_id, key, recipient):
    dmail = Dmail(account_id, key, recipient)
    await dmail.send_mail()


async def create_safe(account_id, key, recipient):
    gnosis_safe = GnosisSafe(account_id, key, recipient)
    await gnosis_safe.create_safe()


async def deploy_contract(account_id, key, recipient):
    deployer = Deployer(account_id, key, recipient)
    await deployer.deploy_token()

def get_tx_count():
    asyncio.run(check_tx())
