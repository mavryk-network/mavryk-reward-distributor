import json
import os
from os.path import dirname, join, normpath
from urllib.parse import urlparse
from unittest.mock import MagicMock
from http import HTTPStatus
from model.reward_provider_model import RewardProviderModel
from typing import Optional
from src.Constants import (
    CONFIG_DIR,
    DEFAULT_LOG_FILE,
    TEMP_TEST_DATA_DIR,
)
from src.util.exit_program import exit_program, ExitCode


class Args:
    """This is a dummy class representing any --arguments passed
    on the command line. You can instantiate this class and then
    change any parameters for testing
    """

    def __init__(
        self,
        initial_cycle,
        reward_data_provider,
        node_addr_public=None,
        api_base_url=None,
    ):
        self.initial_cycle = initial_cycle
        self.run_mode = 3
        self.payment_offset = 0
        self.network = None
        self.node_endpoint = ""
        self.signer_endpoint = ""
        self.reward_data_provider = reward_data_provider
        self.node_addr_public = node_addr_public
        self.base_directory = join(
            dirname(__file__), normpath(TEMP_TEST_DATA_DIR), reward_data_provider
        )
        self.config_dir = join(self.base_directory, normpath(CONFIG_DIR))
        self.log_file = join(self.base_directory, normpath(DEFAULT_LOG_FILE))
        self.dry_run = True
        self.executable_dirs = dirname(__file__)
        self.docker = False
        self.background_service = False
        self.do_not_publish_stats = False
        self.retry_injected = False
        self.verbose = True
        self.api_base_url = api_base_url


def make_config(
    baking_address,
    payment_address,
    service_fee,
    min_delegation_amt,
    min_payment_amt,
):
    """This helper function creates a YAML validators config

    Args:
        baking_address (str): The baking address.
        payment_address (str): The payment address.
        service_fee (float): The service fee.
        min_delegation_amt (int): The minimum amount of deligations.
        min_payment_amt (int): The minimum amount of payments.

    Returns:
        str: Yaml file configuration string.
    """
    return """
    baking_address: {:s}
    delegator_pays_ra_fee: true
    delegator_pays_xfer_fee: true
    founders_map:
        mv1Bm6GciQqJiKHvm7BvCZoFsZ4YejxTpVpY: 0.25
        mv1KscSac2FXLeksvSChMMaHB8o1p7eJccg3: 0.75
    min_delegation_amt: {:d}
    min_payment_amt: {:d}
    owners_map:
        mv1F1uHGUvp6DwfokBqMddz6mPZ7imjjg9X5: 1.0
    payment_address: {:s}
    reactivate_zeroed: true
    rewards_type: actual
    pay_denunciation_rewards: false
    rules_map:
        mv1AmXUYnrqp9pwtaFVYwbxRHDVNbEWiSYAw: mv1BhzVeMiwojX8h8TZ5RBnhDbgZe76U3X3w
        mv1F1uHGUvp6DwfokBqMddz6mPZ7imjjg9X5: TOB
        mindelegation: TOB
    service_fee: {:f}
    specials_map: {{}}
    supporters_set: !!set {{}}
    plugins:
        enabled:
    """.format(
        baking_address,
        min_delegation_amt,
        min_payment_amt,
        payment_address,
        service_fee,
    )


def mock_request_get(url, timeout, **kwargs):
    path = urlparse(url).path
    # print("Mock URL: {}".format(path))

    if path == "/chains/main/blocks/head":
        return MagicMock(
            status_code=HTTPStatus.OK,
            json=lambda: {
                "metadata": {
                    "level_info": {
                        "level": 250000,
                        "level_position": 249999,
                        "cycle": 62,
                    }
                }
            },
        )
    if path == "/chains/main/blocks/2035713/context/raw/json/cycle/500/roll_snapshot":
        return MagicMock(status_code=HTTPStatus.OK, json=lambda: 10)
    if path in [
        "/chains/main/blocks/250000/context/delegates/mv1ATo99QyhrXwvsqHMeuwJ4FiRUJ4NopoGJ",
        "/chains/main/blocks/191232/context/delegates/mv1ATo99QyhrXwvsqHMeuwJ4FiRUJ4NopoGJ",
        "/chains/main/blocks/195328/context/delegates/mv1ATo99QyhrXwvsqHMeuwJ4FiRUJ4NopoGJ",
        "/chains/main/blocks/2034432/context/delegates/mv1ATo99QyhrXwvsqHMeuwJ4FiRUJ4NopoGJ",
        "/chains/main/blocks/2035713/context/delegates/mv1ATo99QyhrXwvsqHMeuwJ4FiRUJ4NopoGJ",
    ]:
        return MagicMock(
            status_code=HTTPStatus.OK,
            json=lambda: {
                "balance": "15218028669",
                "delegating_balance": "191368330803",
                "delegated_contracts": [
                    "mv1HrdvtZssXQPHkyScfr95XPzREH8fRstdC",
                    "mv1F1uHGUvp6DwfokBqMddz6mPZ7imjjg9X5",
                    "mv1DqPoFa2cK2CDTuyyMua2gzPGWVgZixJEU",
                    "mv1GUckNUECJfoz6Xj4Mwe2Wa3WVdyvF6vLE",
                    "mv1G2ShgKy4WzXazyfdnC1b1WhiALFJjm8tC",
                    "mv1ATo99QyhrXwvsqHMeuwJ4FiRUJ4NopoGJ",
                    "mv1AmXUYnrqp9pwtaFVYwbxRHDVNbEWiSYAw",
                ],
                "delegated_balance": "176617802134",
            },
        )
    if path in [
        "/chains/main/blocks/250000/context/contracts/mv1HrdvtZssXQPHkyScfr95XPzREH8fRstdC/balance",
        "/chains/main/blocks/195328/context/contracts/mv1HrdvtZssXQPHkyScfr95XPzREH8fRstdC/balance",
        "/chains/main/blocks/191232/context/contracts/mv1HrdvtZssXQPHkyScfr95XPzREH8fRstdC/balance",
        "/chains/main/blocks/head/context/contracts/mv1HrdvtZssXQPHkyScfr95XPzREH8fRstdC/balance",
        "/chains/main/blocks/2034432/context/contracts/mv1HrdvtZssXQPHkyScfr95XPzREH8fRstdC/balance",
        "/chains/main/blocks/2035713/context/contracts/mv1HrdvtZssXQPHkyScfr95XPzREH8fRstdC/balance",
    ]:
        return MagicMock(status_code=HTTPStatus.OK, json=lambda: "25689884573")
    if path in [
        "/chains/main/blocks/250000/context/contracts/mv1F1uHGUvp6DwfokBqMddz6mPZ7imjjg9X5/balance",
        "/chains/main/blocks/191232/context/contracts/mv1F1uHGUvp6DwfokBqMddz6mPZ7imjjg9X5/balance",
        "/chains/main/blocks/head/context/contracts/mv1F1uHGUvp6DwfokBqMddz6mPZ7imjjg9X5/balance",
        "/chains/main/blocks/2034432/context/contracts/mv1F1uHGUvp6DwfokBqMddz6mPZ7imjjg9X5/balance",
        "/chains/main/blocks/195328/context/contracts/mv1F1uHGUvp6DwfokBqMddz6mPZ7imjjg9X5/balance",
        "/chains/main/blocks/2035713/context/contracts/mv1F1uHGUvp6DwfokBqMddz6mPZ7imjjg9X5/balance",
    ]:
        return MagicMock(status_code=HTTPStatus.OK, json=lambda: "62657825729")
    if path in [
        "/chains/main/blocks/250000/context/contracts/mv1DqPoFa2cK2CDTuyyMua2gzPGWVgZixJEU/balance",
        "/chains/main/blocks/191232/context/contracts/mv1DqPoFa2cK2CDTuyyMua2gzPGWVgZixJEU/balance",
        "/chains/main/blocks/head/context/contracts/mv1DqPoFa2cK2CDTuyyMua2gzPGWVgZixJEU/balance",
        "/chains/main/blocks/2034432/context/contracts/mv1DqPoFa2cK2CDTuyyMua2gzPGWVgZixJEU/balance",
        "/chains/main/blocks/195328/context/contracts/mv1DqPoFa2cK2CDTuyyMua2gzPGWVgZixJEU/balance",
        "/chains/main/blocks/2035713/context/contracts/mv1DqPoFa2cK2CDTuyyMua2gzPGWVgZixJEU/balance",
    ]:
        return MagicMock(status_code=HTTPStatus.OK, json=lambda: "24916325758")
    if path in [
        "/chains/main/blocks/250000/context/contracts/mv1GUckNUECJfoz6Xj4Mwe2Wa3WVdyvF6vLE/balance",
        "/chains/main/blocks/191232/context/contracts/mv1GUckNUECJfoz6Xj4Mwe2Wa3WVdyvF6vLE/balance",
        "/chains/main/blocks/head/context/contracts/mv1GUckNUECJfoz6Xj4Mwe2Wa3WVdyvF6vLE/balance",
        "/chains/main/blocks/2034432/context/contracts/mv1GUckNUECJfoz6Xj4Mwe2Wa3WVdyvF6vLE/balance",
        "/chains/main/blocks/195328/context/contracts/mv1GUckNUECJfoz6Xj4Mwe2Wa3WVdyvF6vLE/balance",
        "/chains/main/blocks/2035713/context/contracts/mv1GUckNUECJfoz6Xj4Mwe2Wa3WVdyvF6vLE/balance",
    ]:
        return MagicMock(status_code=HTTPStatus.OK, json=lambda: "55646701807")
    if path in [
        "/chains/main/blocks/250000/context/contracts/mv1G2ShgKy4WzXazyfdnC1b1WhiALFJjm8tC/balance",
        "/chains/main/blocks/191232/context/contracts/mv1G2ShgKy4WzXazyfdnC1b1WhiALFJjm8tC/balance",
        "/chains/main/blocks/195328/context/contracts/mv1G2ShgKy4WzXazyfdnC1b1WhiALFJjm8tC/balance",
        "/chains/main/blocks/head/context/contracts/mv1G2ShgKy4WzXazyfdnC1b1WhiALFJjm8tC/balance",
        "/chains/main/blocks/2034432/context/contracts/mv1G2ShgKy4WzXazyfdnC1b1WhiALFJjm8tC/balance",
        "/chains/main/blocks/2035713/context/contracts/mv1G2ShgKy4WzXazyfdnC1b1WhiALFJjm8tC/balance",
    ]:
        return MagicMock(status_code=HTTPStatus.OK, json=lambda: "981635036")
    if path in [
        "/chains/main/blocks/250000/context/contracts/mv1ATo99QyhrXwvsqHMeuwJ4FiRUJ4NopoGJ/balance",
        "/chains/main/blocks/191232/context/contracts/mv1ATo99QyhrXwvsqHMeuwJ4FiRUJ4NopoGJ/balance",
        "/chains/main/blocks/195328/context/contracts/mv1ATo99QyhrXwvsqHMeuwJ4FiRUJ4NopoGJ/balance",
        "/chains/main/blocks/head/context/contracts/mv1ATo99QyhrXwvsqHMeuwJ4FiRUJ4NopoGJ/balance",
        "/chains/main/blocks/2034432/context/contracts/mv1ATo99QyhrXwvsqHMeuwJ4FiRUJ4NopoGJ/balance",
        "/chains/main/blocks/2035713/context/contracts/mv1ATo99QyhrXwvsqHMeuwJ4FiRUJ4NopoGJ/balance",
    ]:
        return MagicMock(status_code=HTTPStatus.OK, json=lambda: "30527208")
    if path in [
        "/chains/main/blocks/250000/context/contracts/mv1AmXUYnrqp9pwtaFVYwbxRHDVNbEWiSYAw/balance",
        "/chains/main/blocks/191232/context/contracts/mv1AmXUYnrqp9pwtaFVYwbxRHDVNbEWiSYAw/balance",
        "/chains/main/blocks/195328/context/contracts/mv1AmXUYnrqp9pwtaFVYwbxRHDVNbEWiSYAw/balance",
        "/chains/main/blocks/head/context/contracts/mv1AmXUYnrqp9pwtaFVYwbxRHDVNbEWiSYAw/balance",
        "/chains/main/blocks/2034432/context/contracts/mv1AmXUYnrqp9pwtaFVYwbxRHDVNbEWiSYAw/balance",
        "/chains/main/blocks/2035713/context/contracts/mv1AmXUYnrqp9pwtaFVYwbxRHDVNbEWiSYAw/balance",
    ]:
        return MagicMock(status_code=HTTPStatus.OK, json=lambda: "6725429231")
    if path in [
        "/chains/main/blocks/225280/metadata",
        "/chains/main/blocks/212992/metadata",
        "/chains/main/blocks/2052096/metadata",
        "/chains/main/blocks/4374528/metadata",
    ]:
        return MagicMock(
            status_code=HTTPStatus.OK,
            json=lambda: {
                "balance_updates": [
                    {
                        "kind": "freezer",
                        "category": "deposits",
                        "delegate": "mv1ATo99QyhrXwvsqHMeuwJ4FiRUJ4NopoGJ",
                        "cycle": 51,
                        "change": "-14272000000",
                    },
                    {
                        "kind": "freezer",
                        "category": "fees",
                        "delegate": "mv1ATo99QyhrXwvsqHMeuwJ4FiRUJ4NopoGJ",
                        "cycle": 51,
                        "change": "-8374",
                    },
                    {
                        "kind": "freezer",
                        "category": "rewards",
                        "delegate": "mv1ATo99QyhrXwvsqHMeuwJ4FiRUJ4NopoGJ",
                        "cycle": 51,
                        "change": "-354166658",
                    },
                    {
                        "kind": "contract",
                        "contract": "mv1ATo99QyhrXwvsqHMeuwJ4FiRUJ4NopoGJ",
                        "change": "14626175032",
                    },
                ]
            },
        )
    if path in [
        "/chains/main/blocks/196609/helpers/baking_rights",
        "/chains/main/blocks/2035713/helpers/baking_rights",
        "/chains/main/blocks/head/helpers/baking_rights",
    ]:
        # return empty list - not accurate for estimated reward calculation.
        # However, we do not test for this. We just have to return something
        # so the model gets filled with data.
        return MagicMock(status_code=HTTPStatus.OK, json=lambda: [])
    if path == "/chains/main/blocks/196609/helpers/endorsing_rights":
        # return emtpy list - same comment as above
        return MagicMock(status_code=HTTPStatus.OK, json=lambda: [])

    if path in [
        "/chains/main/blocks/head/context/raw/json/cycle/557/total_active_stake"
    ]:
        return MagicMock(status_code=HTTPStatus.OK, json=lambda: "714705251070165")

    if path in [
        "/chains/main/blocks/head/context/raw/json/cycle/557/selected_stake_distribution"
    ]:
        return MagicMock(
            status_code=HTTPStatus.OK,
            json=lambda: [
                {
                    "validator": "mv1DYzNBa1zgmgQieaQKzLxU1sV3aQSArNJ2",
                    "active_stake": "113536492278227",
                },
                {
                    "validator": "mv1ATo99QyhrXwvsqHMeuwJ4FiRUJ4NopoGJ",
                    "active_stake": "46585432313415",
                },
            ],
        )

    if path in [
        "/chains/main/blocks/head/context/delegates/mv1ATo99QyhrXwvsqHMeuwJ4FiRUJ4NopoGJ"
    ]:
        return MagicMock(
            status_code=HTTPStatus.OK,
            json=lambda: {
                "full_balance": "1474309958894",
                "current_frozen_deposits": "1469667294622",
                "frozen_deposits": "1469667294622",
                "delegating_balance": "14813298160131",
                "delegated_contracts": [
                    "mv19SMJjs82hrufpJbuC3975e4TD4U3ZanrH",
                    "mv19EpZEoF5w8YGVsCS8ueGr6g4q8qDXrHsd",
                ],
                "delegated_balance": "13338988201237",
                "deactivated": False,
                "grace_period": 564,
                "voting_power": "14811963201894",
                "remaining_proposals": 20,
                "active_consensus_key": "mv1FLSR4ExbtVk4DSdq9N9hFnQ8GxSFQQuov",
            },
        )

    if path in [
        "/chains/main/blocks/head/context/contracts/mv19SMJjs82hrufpJbuC3975e4TD4U3ZanrH/balance",
        "/chains/main/blocks/head/context/contracts/mv19EpZEoF5w8YGVsCS8ueGr6g4q8qDXrHsd/balance",
    ]:
        return MagicMock(status_code=HTTPStatus.OK, json=lambda: "9108283")

    if path in [
        "/chains/main/blocks/2981888/metadata",
    ]:
        return MagicMock(
            status_code=HTTPStatus.OK,
            json=lambda: {
                "balance_updates": [
                    {
                        "kind": "freezer",
                        "category": "deposits",
                        "delegate": "mv19SMJjs82hrufpJbuC3975e4TD4U3ZanrH",
                        "cycle": 51,
                        "change": "-14272000000",
                    },
                    {
                        "kind": "freezer",
                        "category": "fees",
                        "delegate": "mv19SMJjs82hrufpJbuC3975e4TD4U3ZanrH",
                        "cycle": 51,
                        "change": "-8374",
                    },
                    {
                        "kind": "freezer",
                        "category": "rewards",
                        "delegate": "mv19SMJjs82hrufpJbuC3975e4TD4U3ZanrH",
                        "cycle": 51,
                        "change": "-354166658",
                    },
                    {
                        "kind": "contract",
                        "contract": "mv19SMJjs82hrufpJbuC3975e4TD4U3ZanrH",
                        "change": "14626175032",
                    },
                ]
            },
        )

    raise Exception(f"Mocked URL not found for path: {path}")


class Constants:
    MAINNET_ADDRESS_DELEGATOR = "mv1Mg1fDVxLHvbE1WhNJZz1N6bKo5edsDQw1"
    MAINNET_ADDRESS_FOUNDATION_0_VALIDATOR = "mv1T9xoFWkkNgy6wH5xeDg9XgdwnqznpuDXs"
    MAINNET_ADDRESS_FOUNDATION_1_VALIDATOR = "mv1CjNm5kcHDBKs5ZwaejxzMUcMVvNGyLC9D"
    BASENET_ADDRESS_FOUNDATION_0_VALIDATOR = "mv1V4h45W3p4e1sjSBvRkK2uYbvkTnSuHg8g"
    MAINNET_ADDRESS_FOUNDATION_1_PAYOUT = "mv1PAYPcHEhXqwVcFei4zfsJvhtDp3Bi63BZ"
