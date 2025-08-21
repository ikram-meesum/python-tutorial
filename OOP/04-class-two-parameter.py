class Student():
    # constructor
    def __init__(self, fullname, myage):
        self.name = fullname
        self.age = myage


s1 = Student("Ahmed Ali", 36)
print(f"My name is {s1.name} and i am {s1.age} years old")
