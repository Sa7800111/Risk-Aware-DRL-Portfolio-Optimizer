import psutil

class ResourceChecker:
    def get_system_load(self):
        return psutil.cpu_percent(), psutil.virtual_memory().percent