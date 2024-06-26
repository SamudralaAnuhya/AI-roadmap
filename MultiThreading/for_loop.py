# Create any multithreaded code using
# for loop for creating multithreads
# for i in range(10):
#     th = Thread(target=func_name, args=(i,))

import threading

# def mul_1(i):
#     for i in range(10):
#         th = threading.Thread(target=mul_1 , args=(i,))
#         th.start()
#     print("Current Threads: %i." % threading.active_count())


import time
import threading
from threading import Thread

def count(i):
    print("Thread %i is sleeping..." %i)
    time.sleep(2)
    print("Thread %i is running actively..." % i)

for i in range (10):
    th=Thread(target=count,args=(i, ))
    th.start()
    print("current thread is %i" % threading.active_count())


