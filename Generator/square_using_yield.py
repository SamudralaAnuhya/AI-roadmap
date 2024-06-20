# Print Square Sequence using yield
#     Create Generator method such that every time it will returns a next square number
#
# for exmaple : 1 4 9 16 ..

def square_using_yield():
    a=1
    while True:
        yield a * a
        a+=1

for n in square_using_yield():
    if n>10:
        break
    print(n)


