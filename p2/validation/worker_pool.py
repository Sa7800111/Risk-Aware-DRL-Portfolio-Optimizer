from multiprocessing import Pool

class DiscoveryWorkers:
    def map_jobs(self, func, data_list):
        with Pool(processes=8) as pool:
            return pool.map(func, data_list)