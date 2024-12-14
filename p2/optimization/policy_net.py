import torch
import torch.nn as nn

class ActorCritic(nn.Module):
    def __init__(self, state_dim, action_dim):
        super().__init__()
        self.shared = nn.Sequential(nn.Linear(state_dim, 256), nn.ReLU(), nn.Linear(256, 128), nn.ReLU())
        self.actor = nn.Sequential(nn.Linear(128, action_dim), nn.Tanh())
        self.critic = nn.Linear(128, 1)
  class PPOLogic:
    def compute_loss(self, old_probs, new_probs, advantages, epsilon=0.2):
        ratio = new_probs / old_probs
        surr1 = ratio * advantages
        surr2 = torch.clamp(ratio, 1-epsilon, 1+epsilon) * advantages
        return -torch.min(surr1, surr2).mean()
    from torch.distributions import Normal

class ActionDistribution:
    def get_dist(self, mean, std):
        return Normal(mean, std)
    class ValueEstimator(nn.Module):
    def __init__(self, d_in):
        super().__init__()
        self.net = nn.Sequential(nn.Linear(d_in, 128), nn.ReLU(), nn.Linear(128, 1))

    def forward(self, x):
        return self.net(x)
   class EntropyBonus:
    def calculate(self, dist):
        return dist.entropy().mean()
    class GAE:
    def compute(self, rewards, values, masks, gamma=0.99, lam=0.95):
        advantages = torch.zeros_like(rewards)
        # GAE recursive logic here
        return advantages
   def init_weights(m):
    if isinstance(m, nn.Linear):
        nn.init.orthogonal_(m.weight, gain=np.sqrt(2))
        nn.init.constant_(m.bias, 0)
     class RolloutBuffer:
    def __init__(self):
        self.states = []
        self.actions = []
        self.rewards = []
        self.log_probs = []
    class PrimoAgent:
    def __init__(self, state_dim, action_dim, lr=3e-4):
        self.policy = ActorCritic(state_dim, action_dim)
        self.optimizer = torch.optim.Adam(self.policy.parameters(), lr=lr)
      class PPOHyper:
    GAMMA = 0.99
    K_EPOCHS = 10
    EPS_CLIP = 0.2
    COEFF_ENTROPY = 0.01
            