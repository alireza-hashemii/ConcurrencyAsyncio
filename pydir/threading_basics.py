import threading
import os 



process_id = f"This is the id of current process: {os.getpid()}"

number_of_threads = threading.active_count()
active_thread = threading.current_thread().name

process_data = {
    'Threads': number_of_threads,
    'Active Thread': active_thread,
    'Process Id': process_id
}
print(process_data)



def hello_target():
    print(f"current thread is {threading.current_thread().name}")
 


new_thread = threading.Thread(target=hello_target)
new_thread.start()

total_threads = threading.active_count()
print(threading.current_thread().name)
new_thread.join()

if new_thread.is_alive():
    print(f"Number of threads are(is): {threading.active_count()}")
else:
    print("It was not")

