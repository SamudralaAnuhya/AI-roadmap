#somethimes cpu sits ideal for example in webservices whilke calling for response it sits ideal untill it receive message dyring that time we make cpu to be busy on other task ,...this
# can be done by runnning parallel programs at a time

import threading
import time
def calculate_square(numbers):
    result = []
    for number in numbers:
        result.append(number * number)
    print(result)
    return result

def calculate_cube(numbers):
    result = []
    for number in numbers:
        result.append(number * number * number)
    return result


numbers = [1,2,3435,7567]
calc_time = time.time()
t1= threading.Thread(target=calculate_square, args=(numbers,))
t2 = threading.Thread(target=calculate_cube, args=(numbers,))
t1.start()
t2.start()

t1.join()
t2.join()
print( "time taken to run program is : " , time.time()-calc_time)
a = calculate_square(numbers)
b = calculate_cube(numbers)