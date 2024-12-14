from transformers import get_linear_schedule_with_warmup

class DiscoveryScheduler:
    @staticmethod
    def get_schedule(optimizer, num_warmup_steps, num_training_steps):
        return get_linear_schedule_with_warmup(optimizer, num_warmup_steps, num_training_steps)