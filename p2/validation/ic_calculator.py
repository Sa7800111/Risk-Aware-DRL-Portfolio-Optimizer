from scipy.stats import spearmanr

class InformationCoefficient:
    def compute_rank_ic(self, signals: np.ndarray, returns: np.ndarray):
        ic, p_val = spearmanr(signals, returns)
        return ic, p_val

    def compute_ir(self, ic_series: pd.Series):
        return ic_series.mean() / ic_series.std()