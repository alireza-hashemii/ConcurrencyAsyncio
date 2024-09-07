import asyncio

async def delay(delay_seconds: float) -> float:
    print(f'delay is running for {delay_seconds} second(s)')
    await asyncio.sleep(delay_seconds)
    print(f'delay for {delay_seconds} second(s) is finished')
    return delay_seconds