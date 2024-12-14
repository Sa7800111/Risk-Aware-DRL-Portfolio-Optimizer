import asyncio
from integration.discovery_orchestrator import DiscoveryOrchestrator

async def main():
    print("Pillar 2: Pairwise Discovery Engine Active.")
    engine = DiscoveryOrchestrator()
    while True:
        await engine.poll_new_headlines()
        await asyncio.sleep(60)

if __name__ == "__main__":
    asyncio.run(main())