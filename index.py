import asyncio, time
from listeners.raydium_snipe import raydium_snipe
from listeners.smart_follow import smart_follow

async def main():
    await asyncio.gather(
        raydium_snipe(),
        smart_follow()
    )

asyncio.run(main())
