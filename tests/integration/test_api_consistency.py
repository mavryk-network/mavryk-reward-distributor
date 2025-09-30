import os
import pytest
import vcr
import requests
from src.Constants import DEFAULT_NETWORK_CONFIG_MAP, PUBLIC_NODE_URL, RewardsType
from tests.utils import Constants

# Block APIs
from src.mvkt.mvkt_block_api import MvKTBlockApiImpl

# Reward APIs
from src.mvkt.mvkt_reward_api import MvKTRewardApiImpl

MAINNET_ADDRESS_DELEGATOR = Constants.MAINNET_ADDRESS_DELEGATOR
MAINNET_ADDRESS_FOUNDATION_0_VALIDATOR = Constants.MAINNET_ADDRESS_FOUNDATION_0_VALIDATOR
MAINNET_ADDRESS_FOUNDATION_1_VALIDATOR = Constants.MAINNET_ADDRESS_FOUNDATION_1_VALIDATOR
BASENET_ADDRESS_FOUNDATION_0_VALIDATOR = Constants.BASENET_ADDRESS_FOUNDATION_0_VALIDATOR
MAINNET_ADDRESS_FOUNDATION_1_PAYOUT = Constants.MAINNET_ADDRESS_FOUNDATION_1_PAYOUT

# These tests should not be mocked but test the overall consistency
# accross all mavryk APIs which are available in MRD


@pytest.fixture
def address_block_api_mvkt():
    return MvKTBlockApiImpl(DEFAULT_NETWORK_CONFIG_MAP["MAINNET"])


@vcr.use_cassette(
    "tests/integration/cassettes/api_consistency/test_get_revelation.yaml",
    filter_headers=["X-API-Key", "authorization"],
    decode_compressed_response=True,
)
def test_get_revelation(address_block_api_mvkt):
    assert address_block_api_mvkt.get_revelation(MAINNET_ADDRESS_DELEGATOR)


@vcr.use_cassette(
    "tests/integration/cassettes/api_consistency/test_get_current_cycle_and_level.yaml",
    filter_headers=["X-API-Key", "authorization"],
    decode_compressed_response=True,
)
def test_get_current_cycle_and_level(address_block_api_mvkt):
    cycle_mvkt, level_mvkt = address_block_api_mvkt.get_current_cycle_and_level()

    assert cycle_mvkt == 5


@vcr.use_cassette(
    "tests/integration/cassettes/api_consistency/test_get_delegatable.yaml",
    filter_headers=["X-API-Key", "authorization"],
    decode_compressed_response=True,
)
def test_get_delegatable(address_block_api_mvkt):
    assert address_block_api_mvkt.get_delegatable(MAINNET_ADDRESS_FOUNDATION_0_VALIDATOR)


# NOTE: We are using a testnet validator where we can manage the amount of delegates
@pytest.fixture
def address_reward_api_mvkt():
    return MvKTRewardApiImpl(
        DEFAULT_NETWORK_CONFIG_MAP["MAINNET"], MAINNET_ADDRESS_FOUNDATION_1_VALIDATOR
    )


@vcr.use_cassette(
    "tests/integration/cassettes/api_consistency/test_get_rewards_for_cycle_map.yaml",
    filter_headers=["X-API-Key", "authorization"],
    decode_compressed_response=True,
)
def test_get_rewards_for_cycle_map(
    address_reward_api_mvkt,
):
    # NOTE: There is currently a level limit query with rpc when querying endorsing rewards in the past
    # thus we are disabling the consistency check with other APIs for now but will hopefully reenable it in the future

    last_cycle = 5
    rewards_mvkt = address_reward_api_mvkt.get_rewards_for_cycle_map(
        cycle=last_cycle, rewards_type=RewardsType.ACTUAL
    )

    # Check delegator_balance_dict
    assert len(rewards_mvkt.delegator_balance_dict) == 8
    total_delegated_balance = 0
    for (
        mvkt_delegator_adress,
        mvkt_balance_dict,
    ) in rewards_mvkt.delegator_balance_dict.items():
        assert mvkt_balance_dict["current_balance"] == 257  # the same for each delegate
        total_delegated_balance += mvkt_balance_dict["delegated_balance"]
    assert total_delegated_balance == rewards_mvkt.external_delegated_balance

    # Own delegate balance
    assert rewards_mvkt.own_delegated_balance == 9_137_159_953_145

    # Check num_baking_rights
    assert rewards_mvkt.num_baking_rights == 3289

    # Check denunciation_rewards
    assert rewards_mvkt.denunciation_rewards == 0

    # Check equivocation_losses
    assert rewards_mvkt.equivocation_losses == 0

    # Check offline_losses
    assert rewards_mvkt.offline_losses == 0

    # Check potential_endorsement_rewards
    assert rewards_mvkt.potential_endorsement_rewards == 21_822_738_840

    # Check rewards_and_fees
    assert rewards_mvkt.rewards_and_fees == 9_479_008_394

    # Check computed_reward_amount
    assert rewards_mvkt.computed_reward_amount is None
