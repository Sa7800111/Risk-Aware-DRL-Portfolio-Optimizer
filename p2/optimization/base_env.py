import gymnasium as gym
from gymnasium import spaces
import numpy as np

class PrimoTradingEnv(gym.Env):
    def __init__(self, data_stream, initial_balance=100000):
        super().__init__()
        self.data = data_stream
        self.initial_balance = initial_balance
        self.action_space = spaces.Box(low=-1, high=1, shape=(1,), dtype=np.float32)
        self.observation_space = spaces.Box(low=-np.inf, high=np.inf, shape=(16,), dtype=np.float32)
        class StateAssembler:
    def build_vector(self, market_obs, nlp_tensor, portfolio_stats):
        state = np.concatenate([
            market_obs,      
            nlp_tensor,      
            portfolio_stats  
        ])
        return state.astype(np.float32)
    class RewardShaper:
    def __init__(self, risk_aversion=0.1):
        self.lambda_ = risk_aversion

    def calculate(self, pnl, drawdown, volatility):
        return pnl - (self.lambda_ * drawdown) - (0.01 * volatility)
    class PortfolioTracker:
    def __init__(self, cash):
        self.cash = cash
        self.shares = 0
        self.total_value = cash

    def update(self, price, action_val):
        self.total_value = self.cash + (self.shares * price)
   class MarketStreamer:
    def __init__(self, df):
        self.df = df
        self.current_idx = 0

    def next_obs(self):
        obs = self.df.iloc[self.current_idx]
        self.current_idx += 1
        return obs
    class ObsNormalizer:
    def __init__(self, epsilon=1e-8):
        self.mean = 0
        self.std = 1
        self.eps = epsilon

    def scale(self, x):
        return (x - self.mean) / (self.std + self.eps)
    class ActionScaler:
    def scale_to_shares(self, action, cash, price):
        target_value = (action + 1) / 2 * cash
        return int(target_value / price)
    class TerminationLogic:
    def is_done(self, balance, initial_balance, step, max_steps):
        if balance < initial_balance * 0.5: return True
        if step >= max_steps: return True
        return False
    class StepLogger:
    def __init__(self):
        self.history = []

    def log(self, step, reward, pnl):
        self.history.append({"s": step, "r": reward, "p": pnl})
        class EnvConfig:
    MAX_STEPS = 252
    FEES = 0.001
    SLIPPAGE = 0.0005
    INITIAL_CASH = 100000
    class Technicals:
    def get_rsi(self, prices, window=14):
        delta = np.diff(prices)
        return 100 - (100 / (1 + np.mean(delta[delta > 0]) / -np.mean(delta[delta < 0])))
    class StateBuffer:
    def __init__(self, capacity=5):
        self.buffer = []
        self.capacity = capacity

    def push(self, state):
        self.buffer.append(state)
        if len(self.buffer) > self.capacity: self.buffer.pop(0)
    class MultiAssetPrimoEnv(PrimoTradingEnv):
    def __init__(self, assets):
        super().__init__(assets)
        self.action_space = spaces.Box(low=-1, high=1, shape=(len(assets),))
    class EnvWrappers:
    @staticmethod
    def wrap_monitor(env):
        return gym.wrappers.RecordEpisodeStatistics(env)
    class ResetHandler:
    def perform_reset(self, env):
        env.current_step = 0
        env.portfolio = PortfolioTracker(env.initial_balance)
        return env.observation_space.sample()
    class CostModel:
    def calculate(self, qty, price, fee_rate):
        return qty * price * fee_rate
    class EnvValidator:
    def check_nans(self, state):
        return np.isnan(state).any()
    class TickerMap:
    def __init__(self, tickers):
        self.map = {t: i for i, t in enumerate(tickers)}
    class EnvRenderer:
    def render(self, mode="human"):
        pass
    def make_primo_env(data):
    env = PrimoTradingEnv(data)
    return gym.wrappers.FlattenObservation(env)
