import torch

class OrderImageGen:
    def __init__(self, bins: int = 64):
        self.bins = bins

    def generate_image(self, orders, mid_price: float):
        img = torch.zeros((3, self.bins, self.bins))
        for o in orders:
            p_idx = int(np.clip((o.price - mid_price) * 100 + self.bins//2, 0, self.bins-1))
            v_idx = int(np.clip(np.log1p(o.qty), 0, self.bins-1))
            channel = 0 if o.side == Side.BUY else 1
            img[channel, p_idx, v_idx] += 1
        return img / img.max() if img.max() > 0 else img