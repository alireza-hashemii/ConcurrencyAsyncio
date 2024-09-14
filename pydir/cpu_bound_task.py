import threading
import os 
import time

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




def prinf_fib(number: int):
    def fibonacci(n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 1
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)
    print(f"Fibonacci of {number} is {fibonacci(number)}")
        
def call_to_fib():
    fourtieth_thread = threading.Thread(target=prinf_fib(40)) 
    thirtininth = threading.Thread(target=prinf_fib(39)) 
    fourtieth_thread.start()
    thirtininth.start()

    fourtieth_thread.join()
    fourtieth_thread.join()

start = time.time()
call_to_fib()
end = time.time()

print(f"Whole operation took {end - start} seconds.")