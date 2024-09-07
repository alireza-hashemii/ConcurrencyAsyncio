import asyncio

async def add_one_unt(number: int):
    return number + 1

done = add_one_unt(1)
print(done)
print(type(done))