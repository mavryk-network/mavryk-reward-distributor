from enum import Enum
from datetime import date

# General
VERSION = 12.0
PYTHON_MAJOR = 3
PYTHON_MINOR = 8
LINER = "--------------------------------------------"

# Disabled or enabled options by developers
ALLOWED_REWARD_DATA_PROVIDER_CHOICES = ["mvkt"]

# Persistent data directories
BASE_DIR = "~/pymnt"
CONFIG_DIR = "cfg"
SIMULATIONS_DIR = "simulations"
REPORTS_DIR = "reports"
DEFAULT_LOG_FILE = "logs/app.log"
TEMP_TEST_DATA_DIR = "__TEMP_DATA__"
REQUIREMENTS_FILE_PATH = "requirements.txt"

# potentially the next upgrade
NEW_PROTOCOL_DATE = date(2026, 12, 31)
NEW_PROTOCOL_NAME = "C"

LOCAL_HOST = "127.0.0.1"
EXIT_PAYMENT_TYPE = "exit"
# TESTNET_PREFIX = "base"
TESTNET_PREFIX = "atlas"
TESTNET_SUFFIX = "net"
CURRENT_TESTNET = (TESTNET_PREFIX + TESTNET_SUFFIX).upper()


MAX_SEQUENT_CALLS = 256  # to prevent possible endless looping

FIRST_BOREAS_LEVEL = 32769

FIRST_C_LEVEL = 9999999

MAVRYK_RPC_PORT = 8732

SIGNER_PORT = 6732

# Attention: We do not use a lib to join URLs
# Join them like this:
# >>> url = "http://base" + "/append" # look at the "/" of the appending part

# Local URLs
PRIVATE_SIGNER_URL = "http://{}:{}".format(LOCAL_HOST, SIGNER_PORT)
PRIVATE_NODE_URL = "http://{}:{}".format(LOCAL_HOST, MAVRYK_RPC_PORT)

# Public RPC
PUBLIC_NODE_URL = {
    "MAINNET": "https://rpc.mavryk.network",
    # CURRENT_TESTNET: "https://basenet.rpc.mavryk.network",
    CURRENT_TESTNET: "https://atlasnet.rpc.mavryk.network",
}

# MvKT
MVKT_PUBLIC_API_URL = {
    "MAINNET": "https://api.mavryk.network/v1",
    CURRENT_TESTNET: "https://{}.api.mavryk.network/v1".format(CURRENT_TESTNET.lower()),
}

# Network Constants
# ------------------------
#
# Mainnet:
# https://rpc.mavryk.network/chains/main/blocks/head/context/constants
#
# Testnet:
# https://basenet.rpc.mavryk.network/chains/main/blocks/head/context/constants
DEFAULT_NETWORK_CONFIG_MAP = {
    "MAINNET": {
        # General
        "NAME": "MAINNET",
        "MINIMAL_BLOCK_DELAY": 10,
        "BLOCKS_PER_CYCLE": 24576,
    },
    CURRENT_TESTNET: {
        # General
        "NAME": CURRENT_TESTNET,
        "MINIMAL_BLOCK_DELAY": 5,
        "BLOCKS_PER_CYCLE": 12288,
    },
}

MUMAV_PER_MAV = 1e6

MAXIMUM_ROUNDING_ERROR = 10  # mumav
ALMOST_ZERO = 1e-6
DISK_LIMIT_PERCENTAGE = 0.1
GIGA_BYTE = 1e9
DISK_LIMIT_SIZE = 5 * GIGA_BYTE

PKH_LENGTH = 36

BUF_SIZE = 50


class DryRun(str, Enum):
    SIGNER = "SIGNER"
    NO_SIGNER = "NO_SIGNER"


class RunMode(Enum):
    FOREVER = 1
    PENDING = 2
    ONETIME = 3
    RETRY_FAILED = 4


class PaymentStatus(Enum):
    """
    PAID: payment successfully made.
    FAIL: Some failures happened in the process.
    DONE: Process completed without payment. E.g. zero amount, dry run...
    INJECTED: Transaction is injected into the node but after waiting for some time it is not added to any block.
    AVOIDED: payment item avoided because of lack of support, incompatibility of contract script,
             contract with no default entry point, too high fees, liquidated contract, etc.
    MRD does not know its fate.
    """

    UNDEFINED = -1
    FAIL = 0
    PAID = 1
    DONE = 2
    INJECTED = 3
    AVOIDED = 4

    def is_undefined(self):
        return self.value == -1

    def is_fail(self):
        return self.value == 0

    def is_paid(self):
        return self.value == 1

    def is_done(self):
        return self.value == 2

    def is_injected(self):
        return self.value == 3

    def is_avoided(self):
        return self.value == 4

    def is_processed(self):
        return self.value > 0

    def __str__(self):
        return self.name


class RewardsType(Enum):
    ACTUAL = "actual"
    IDEAL = "ideal"
    ESTIMATED = "estimated"

    def isEstimated(self):
        return self == RewardsType.ESTIMATED

    def isActual(self):
        return self == RewardsType.ACTUAL

    def isIdeal(self):
        return self == RewardsType.IDEAL

    def __str__(self):
        return self.value
