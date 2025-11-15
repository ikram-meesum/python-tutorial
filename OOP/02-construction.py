# ========== INIT CONSTRUCT METHOD ===========

# A function that’s part of a class is a method. The __init__() method 2 is a special
# method that runs automatically whenever we create a new instance based on the class.
# This method has two underscores on each side of __init__().
# The self parameter is required in the method definition, and it must come first,
# before the other parameters.


class Dog():
    # constructor
    def __init__(self):
        print(self)
        print("constructor funciton call")


dog1 = Dog()
print(dog1)


# 02 Example of constructor


class Student:
    def start_learning(self):
        print("Learning started")

    # No need to called the constructed method and execute first
    def __init__(self):
        print('Instant method called')


std = Student()
std.start_learning()

# Get all class attributes only using __dict__


class Employee:
    def __init__(self, name, empAge, empSalary):
        self.empName = name
        self.age = empAge
        self.salary = empSalary

    def test2():
        print('test method')


emp = Employee('Mohammad Ali', 45, 125000)
print(emp.__dict__)
