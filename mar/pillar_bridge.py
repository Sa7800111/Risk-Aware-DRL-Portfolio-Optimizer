class PillarConnector:
    def __init__(self, mars, discovery, primo):
        self.mars = mars
        self.discovery = discovery
        self.primo = primo

    def execute_unified_step(self, news_text: str):
        nlp_features = self.discovery.process(news_text)
        action = self.primo.get_action(nlp_features)
        return self.mars.inject_user_order(action)