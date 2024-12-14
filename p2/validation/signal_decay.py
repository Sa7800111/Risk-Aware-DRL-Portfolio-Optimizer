class DecayAnalyzer:
    def calculate_half_life(self, signal_series: pd.Series, price_series: pd.Series):
        corrs = []
        for lag in range(1, 21):
            corrs.append(signal_series.corr(price_series.shift(-lag)))
        
        corrs = np.array(corrs)
        half_life = np.where(corrs < corrs[0] / 2)[0]
        return half_life[0] if len(half_life) > 0 else 20