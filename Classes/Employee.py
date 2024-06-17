# Create a sample class named Employee with two attributes id and name
# employee :
#     id
#     name
# object initializes id and name dynamically for every Employee object created.
#
# emp = Employee(1, "coder")
# Use del property to first delete id attribute and then the entire object

class Employe():
    def __init__(self , id , name ):
        self.id = id
        self.name = name

    def display(self):
        print(f"ID : {self.id} \n Name : {self.name}")

emp =  Employe(1, "coder")
emp.display()
del emp.id
try :
    print(emp.id)
except AttributeError:
    del emp
    print("Employee is not defined")