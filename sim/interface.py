import asyncio
from typing import List, Dict, Any
from core.system_gateway import MarsGateway
from lmm.inference_engine import LMMInference

class MarSInterface:
    def __init__(self, gateway: MarsGateway, inference: LMMInference):
        self.gateway = gateway
        self.inference = inference
        self.active_scenarios = {}

    async def run_interactive_session(self, ticker: str, duration_sec: int):
        start_time = time.time()
        while time.time() - start_time < duration_sec:
            state = self.gateway.state.books[ticker].get_depth(10)
            tokens = self.inference.generate_next_batch(state)
            for cmd in tokens:
                self.gateway.handle_request(ticker, cmd)
            await asyncio.sleep(0.01)