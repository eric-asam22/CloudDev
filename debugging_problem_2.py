"""

Problem Statement:
This Python program implements a multi-threaded queue processor. The program is supposed to process tasks from a shared queue using multiple threads, but there seems to be a synchronization issue causing occasional data corruption.

Tasks:

Identify and fix the bug causing data corruption in the shared queue.
Ensure proper synchronization mechanisms are in place to prevent race conditions and ensure data integrity.
Optimize the program for efficiency and scalability if possible.

"""

import threading
import queue
import time

# Shared queue
task_queue = queue.Queue()

# Worker function
def worker():
    while True:
        if not task_queue.empty():
            task = task_queue.get()
            # Simulate processing
            print("Processing task:", task)
            time.sleep(0.5)  # Simulate processing time
            task_queue.task_done()

# Create worker threads
for _ in range(5):
    t = threading.Thread(target=worker)
    t.daemon = True
    t.start()

# Add tasks to the queue
for i in range(10):
    task_queue.put(i)

# Wait for all tasks to be processed
task_queue.join()

print("All tasks processed")
