import gymnasium as gym
from gymnasium import spaces

class MarsExecutionEnv(gym.Env):
    def __init__(self, engine: Any, target_qty: int, time_limit: int):
        super().__init__()
        self.engine = engine
        self.target_qty = target_qty
        self.remaining_qty = target_qty
        self.time_limit = time_limit
        self.current_time = 0
        
        self.action_space = spaces.Box(low=0, high=1, shape=(1,), dtype=np.float32)
        self.observation_space = spaces.Box(low=-np.inf, high=np.inf, shape=(12,), dtype=np.float32)

    def step(self, action):
        slice_qty = int(action[0] * self.remaining_qty)
        exec_price = self.engine.execute_market_order(slice_qty)
        
        self.remaining_qty -= slice_qty
        self.current_time += 1
        
        reward = -abs(exec_price - self.engine.get_mid()) * slice_qty
        obs = self.engine.get_state_vector()
        done = self.remaining_qty <= 0 or self.current_time >= self.time_limit
        
        return obs, reward, done, False, {}