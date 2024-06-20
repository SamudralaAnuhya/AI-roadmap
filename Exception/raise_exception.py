# Create a custom exception AdultException.
# Create a class Person with attributes name and age in it.
# Create a function get_minor_age() in the class. It throws an exception if the person is adult otherwise returns age.
# Create a function display_person() which prints the age and name of a person.

class AdultException(Exception):
    pass

class person ():
    def __init__(self , name , age):
        self.age = age
        self.name = name

    def get_minor_age(self):
      if self.age >= 18:
          raise AdultException
      else:
          return self.age

    def display_age(self):
        try:
            print(f"age-->{self.get_minor_age()}")
        except AdultException:
            print("person is adult")
        finally:
            print(f"name-->{self.name}")



person("anu",14).display_age()
person("anuhya",35).display_age()


