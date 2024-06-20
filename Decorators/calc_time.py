#decoraters act as wrapper to the function it helps as function to the other function which menas to to print start and end lines in the he differnect
# fucntions similar and caliculate time and all

import time
def calc_time(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            print(func.__name__ + "took" + str((end - start)*1000) + "milli seconds to execute")
            return result
        return wrapper

@calc_time
def calc_squre(numbers):
    result = []
    for number in numbers:
        result.append(number * number)
    print(result)
    return result

@calc_time
def calc_cube(numbers):
    result = []
    for number in numbers:
        result.append(number * number * number )
    print(result)
    return result



array = range(10)
a = calc_squre(array)
b = calc_cube(array)