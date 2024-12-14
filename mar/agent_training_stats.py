class TrainingLogger:
    def __init__(self):
        self.rewards = []
        self.slippages = []

    def log_episode(self, total_reward, avg_slippage):
        self.rewards.append(total_reward)
        self.slippages.append(avg_slippage)