# Create an iterator for fibonacci series in such a way that each next returns the next element from fibonacci series.
# The iterator should stop when it reaches a limit defined in the constructor.


class Fibonacci:
    def __init__(self , number):
        self.number = number
        self.count = 0
        self.a,self.b = 0,1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.number:
            self.a , self.b = self.b, self.a + self.b
            self.count +=1
            return self.b
        else:
            raise StopIteration


r = Fibonacci(10)
while True:
    try:
        print(next(r))
    except StopIteration:
        break












