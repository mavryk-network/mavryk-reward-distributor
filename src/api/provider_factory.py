from mvkt.mvkt_block_api import MvKTBlockApiImpl
from mvkt.mvkt_reward_api import MvKTRewardApiImpl


class ProviderFactory:
    def __init__(self, provider):
        self.provider = provider

    def newRewardApi(
        self,
        network_config,
        baking_address,
        node_url,
        node_url_public="",
        api_base_url=None,
    ):
        return MvKTRewardApiImpl(network_config, baking_address, base_url=api_base_url)

    def newBlockApi(
        self,
        network_config,
        node_url,
        api_base_url=None,
    ):
        return MvKTBlockApiImpl(network_config, base_url=api_base_url)
