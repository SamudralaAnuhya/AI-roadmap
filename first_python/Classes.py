class Human:
    def __init__(self , n , w) :
        self.name = n
        self.work = w

    def do_work(self):
        if self.work == "Job":
            print(self.name, "is working professional")
        elif self.work == "Actor":
            print(self.name, " is a Actor")
        else:
            print(self.name, "is searching for work")

    def do_speak(self):
        if self.work == "Job":
            print(self.name, "know java , python")
        elif self.work == "Actor":
            print(self.name, "know English ")
        else :
            print(self.name, "intrested in learining any thing")

alice =Human("Alice","Job")
alice.do_work()
alice.do_speak()

tom = Human("Tom","Actor")
tom.do_work()
tom.do_speak()

cruise = Human("Cruise","")
cruise.do_work()
cruise.do_speak()

