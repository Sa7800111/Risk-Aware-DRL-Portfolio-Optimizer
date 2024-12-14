class ImpactAnalysisPlatform:
    def __init__(self, engine: Any):
        self.engine = engine

    def run_what_if(self, base_scenario: dict, injection: dict):
        base_res = self.engine.simulate(base_scenario)
        impact_res = self.engine.simulate({**base_scenario, "injection": injection})
        
        diff = impact_res['prices'] - base_res['prices']
        return {
            "absolute_impact": diff[-1],
            "max_temporary_impact": np.max(np.abs(diff)),
            "permanent_impact": diff[-1]
        }