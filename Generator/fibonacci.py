# 0 ,1 ,1,2, 3, 5 (value , value+previous value)

def fibonacci():
    a, b = 0 , 1
    while True:
        yield a
        a, b = b, a+b

for value in fibonacci():
    if value > 100:
        break
    print(value)



