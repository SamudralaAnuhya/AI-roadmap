#when clicking on next it should go to the next channel til the end and stop
# write iter nd next methods and raise stop iteration

class Remote_control():
    def __init__(self):
        self.channels = ["Gemini", "Maa", "Etv"]
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index >= len(self.channels):
            raise StopIteration
        return self.channels[self.index]


r = Remote_control()
itr = iter(r)
print(next(itr))
print(next(itr))
print(next(itr))

