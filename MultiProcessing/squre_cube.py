#in multi threading the result can disiplay evem outside but in the multipricess output is local it can print outside(evemn in th main)

import multiprocessing
import time
result =[]
def cal_square(numbers):
    for n in numbers:
        result.append(n*n)
    print(result)


if __name__ == "__main__":
    num = [12,5,6]
    p1=multiprocessing.Process(target=cal_square, args=(num,))
    p1.start()
    p1.join()
    print(result)


