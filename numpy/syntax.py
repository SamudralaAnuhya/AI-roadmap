# python stores the memory in 14 bytes where as numpy stores 4 bytes
# fast and easy to use

# lets consider to add 2 lists by using both python syntax and numpy sysntax


import numpy as np
import sys
import time

SIZE = 1000000
# l1 , l2 are the lists for python list , n1 , n2 are the lists for numpy

print(np)
l1 = range(SIZE)
l2 = range(SIZE)

n1 = np.arange(SIZE)
n2 = np.arange(SIZE)

start = time.time()
result = [(x + y) for x, y in zip(l1, l2)]
print("python list comprehension: ", (time.time() - start) * 1000)

start = time.time()
# result = n1+n2
print("numpy list comprehension: ", (time.time() - start) * 1000)
