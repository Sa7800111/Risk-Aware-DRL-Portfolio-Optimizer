class PrimoBridge:
    def __init__(self, primo_agent):
        self.agent = primo_agent

    def feed_obs(self, nlp_tensor):
        return self.agent.predict(nlp_tensor)