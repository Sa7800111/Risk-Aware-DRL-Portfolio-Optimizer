class TrajectorySampler:
    def __init__(self, inference: LMMInference):
        self.inference = inference

    def sample_paths(self, initial_state: dict, n_paths: int = 10, steps: int = 100):
        paths = []
        for _ in range(n_paths):
            current_path = [initial_state['mid']]
            temp_state = initial_state.copy()
            for _ in range(steps):
                next_val = self.inference.predict_single(temp_state)
                current_path.append(next_val)
            paths.append(current_path)
        return paths