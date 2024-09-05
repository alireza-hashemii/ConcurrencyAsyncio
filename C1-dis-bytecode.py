import dis


def myfunc(alist):
    return len(alist)

bytec = dis.Bytecode(myfunc)
for b in bytec:
    print(b)


import time
def print_fib(number: int) -> None:
    def fib(n: int) -> int:
        if n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            return fib(n - 1) + fib(n - 2)
    print(f'fib({number}) is {fib(number)}')

def fibs_no_threading():
    print_fib(40)
    print_fib(41)

start = time.time()
fibs_no_threading()
end = time.time()
print(f'Completed in {end - start:.4f} seconds.')



import threading
import time

def print_fib(number: int) -> None:
 def fib(n: int) -> int:
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
    

def fibs_with_threads():
    fortieth_thread = threading.Thread(target=print_fib, args=(40,))
    forty_first_thread = threading.Thread(target=print_fib, args=(41,))

    fortieth_thread.start()
    forty_first_thread.start()
    fortieth_thread.join()
    forty_first_thread.join()

start_threads = time.time()
fibs_with_threads()

end_threads = time.time()
print(f'Threads took {end_threads - start_threads:.6f} seconds.')



import time
import requests
def read_example() -> None:
 response = requests.get('https://www.google.com')
 print(response.status_code)
sync_start = time.time()
read_example()
read_example()
sync_end = time.time()
print(f'Running synchronously took {sync_end - sync_start:.4f} seconds.')



import time
import threading
import requests
def read_example() -> None:
 response = requests.get('https://www.example.com')
 print(response.status_code)
thread_1 = threading.Thread(target=read_example)
thread_2 = threading.Thread(target=read_example)
thread_start = time.time()
thread_1.start()
thread_2.start()
print('All threads running!')
thread_1.join()
thread_2.join()
thread_end = time.time()
print(f'Running with threads took {thread_end - thread_start:.4f} seconds.')