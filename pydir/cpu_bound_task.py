import threading
import os 
import time
import asyncio

import asyncio

async def delay(delay_seconds: float) -> float:
    print(f'delay is running for {delay_seconds} second(s)')
    await asyncio.sleep(delay_seconds)
    print(f'delay for {delay_seconds} second(s) is finished')
    return delay_seconds

# def prinf_fib(number: int):
#     def fibonacci(n: int) -> int:
#         if n == 1:
#             return 1
#         elif n == 2:
#             return 1
#         else:
#             return fibonacci(n - 1) + fibonacci(n - 2)
#     print(f"Fibonacci of {number} is {fibonacci(number)}")
        
# def call_to_fib():
#     prinf_fib(40)
#     prinf_fib(39)

# start = time.time()
# call_to_fib()
# end = time.time()

# print(f"Whole operation took {end - start} seconds.")




# def prinf_fib(number: int):
#     def fibonacci(n: int) -> int:
#         if n == 1:
#             return 1
#         elif n == 2:
#             return 1
#         else:
#             return fibonacci(n - 1) + fibonacci(n - 2)
#     print(f"Fibonacci of {number} is {fibonacci(number)}")
        
# def call_to_fib():
#     fourtieth_thread = threading.Thread(target=prinf_fib(40)) 
#     thirtininth = threading.Thread(target=prinf_fib(39)) 
#     fourtieth_thread.start()
#     thirtininth.start()

#     fourtieth_thread.join()
#     fourtieth_thread.join()

# start = time.time()
# call_to_fib()
# end = time.time()

# print(f"Whole operation took {end - start} seconds.")



# async def add_one_unit(number):
#     await delay(2)
#     return number + 1

# async def hello_world_msg():
#     await delay(2)
#     return 'Hello, world'

# async def main():
#     rs_add =  asyncio.create_task(add_one_unit(4))
#     rs_msg =  asyncio.create_task(hello_world_msg())

#     await rs_add
#     await rs_msg
  

# asyncio.run(main())

async def getting_cold():
    print('The The tea is getting cold...')
    await delay(4)
    return True

async def coffe_maker():
    print("The machine is making coffe...")
    await delay(2)
    return True

async def main():
    rs_get =  asyncio.create_task(getting_cold())
    rs_coffe =  asyncio.create_task(coffe_maker())

    await rs_coffe
    await rs_get
    # print(rs_coffe)
    # print(rs_get)

start = time.time()
asyncio.run(main())
end = time.time()
print(f"whole operation took about {end - start} second(s)")
