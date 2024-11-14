# RANDOM WALLETS MODE
RANDOM_WALLET = True  # True/False

# removing a wallet from the list after the job is done
REMOVE_WALLET = False

SLEEP_FROM = 7  # Second
SLEEP_TO = 49  # Second

QUANTITY_THREADS = 1

THREAD_SLEEP_FROM = 7
THREAD_SLEEP_TO = 39

# GWEI CONTROL MODE
CHECK_GWEI = True  # True/False
MAX_GWEI = 63.8

MAX_PRIORITY_FEE = {
    "ethereum": 0.1,
    "polygon": 40,
    "arbitrum": 0.1,
    "base": 0.1,
    "zksync": 0.35,
}

GAS_MULTIPLIER = 3
GAS_LIMIT_MULTIPLIER = 1.5

# RETRY MODE
RETRY_COUNT = 3

LAYERSWAP_API_KEY = ""
