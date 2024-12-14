import torch.nn.functional as F

class DiscoveryDistiller:
    def __init__(self, teacher, student, temp=2.0):
        self.teacher = teacher
        self.student = student
        self.temp = temp

    def compute_distill_loss(self, x, attention_mask):
        with torch.no_grad():
            t_logits = self.teacher(x, attention_mask)
        s_logits = self.student(x, attention_mask)
        return F.kl_div(F.log_softmax(s_logits/self.temp), F.softmax(t_logits/self.temp))