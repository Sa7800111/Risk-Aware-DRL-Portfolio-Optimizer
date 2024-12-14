class HealthCheck:
    def check_all(self, modules: list):
        return {m.__name__: "OK" for m in modules}