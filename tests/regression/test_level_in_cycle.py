from src.Constants import DEFAULT_NETWORK_CONFIG_MAP
from src.api.block_api import BlockApi


class DummyApiImpl(BlockApi):
    def __init__(self):
        super(DummyApiImpl, self).__init__(DEFAULT_NETWORK_CONFIG_MAP["MAINNET"])

    def get_current_cycle_and_level(self):
        return 0


def test_levels_in_cycle():

    level_positions = [
        [32769, 0],  # Boreas activation level
        [38988, 647],
    ]

    block = DummyApiImpl()

    for level, pos in level_positions:
        assert block.level_in_cycle(level) == pos
