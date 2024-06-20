# Create multiple inheritance on teacher,student and youtuber.



class Student():
    def student_action(self):
        print("I am student")
class Teacher():
    def teacher_action(self):
        print("I am teacher")

class youtuber():
    def youtuber_action(self):
        print("I am youtuber")

class person(Student , Teacher , youtuber):
    pass

x = person()
x.student_action()
x.teacher_action()
x.youtuber_action()
