class CosineWarmup(torch.optim.lr_scheduler._LRScheduler):
    def __init__(self, optimizer, warmup_steps, total_steps):
        self.warmup = warmup_steps
        self.total = total_steps
        super().__init__(optimizer)

    def get_lr(self):
        step = self._step_count
        if step < self.warmup:
            return [base_lr * step / self.warmup for base_lr in self.base_lrs]
        return [base_lr * 0.5 * (1 + math.cos(math.pi * (step - self.warmup) / (self.total - self.warmup))) for base_lr in self.base_lrs]