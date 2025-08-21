class Student():
    # constructor
    def __init__(self, fullname, myage):
        self.name = fullname
        self.age = myage

    def greetting(self):
        print(f"My name is {self.name} and I am {self.age} years old")


s1 = Student("Ahmed Ali", 36)
s1.greetting()

s2 = Student("Kamran Ali", 27)
s2.greetting()
