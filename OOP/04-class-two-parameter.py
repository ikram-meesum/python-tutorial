class Student():
    # constructor
    def __init__(self, fullname, myage):
        self.name = fullname
        self.age = myage


s1 = Student("Ahmed Ali", 36)
print(f"My name is {s1.name} and i am {s1.age} years old")


# Second example of class parameter


class Student2:
    # No need to called the constructed method but it will be execute first.
    def __init__(self, name, age):
        self.name = name
        self.age = age

        print(f'My name is {name} and my age is {age}.')
        print(f'Second example name is {self.name} and my age is {self.age}.')

    def start_learning(self):
        print("Learning started")


std2 = Student2("Ikram", 40)  # first print
# second print
print(f"Other way the name is {std2.name} and age is {std2.age}.")

std2 = Student2("Ahmed Ali", 63)
print(f"Other way the name is {std2.name} and age is {std2.age}.")
