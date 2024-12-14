class GraphBuilder:
    def build_from_metadata(self, asset_list: list):
        nodes = {}
        for asset in asset_list:
            nodes[asset['ticker']] = AssetNode(asset['ticker'], asset['sector'])
        return nodes