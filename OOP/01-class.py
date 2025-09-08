# Object-oriented programming (OOP) is one of the most effective approaches to writing
# software. In object-oriented programming, you write classes that represent real-world
# things and situations, and you create objects based on these classes.

# Making an object from a class is called instantiation, and you work with instances of
# a class. In this chapter you’ll write classes and create instances of those classes.
# You’ll specify the kind of information that can be stored in instances, and you’ll
# define actions that can be taken with these instances.

# You’ll also write classes that extend the functionality of existing classes, so
# similar classes can share common functionality, and you can do more with less code.
# You’ll store your classes in modules and import classes written into your own
# program files.

# Each instance created from the Dog class will store a name and an age.

# What are the Four Main Principles of OOP
# The four pillars of OOP are:

# Encapsulation
# Abstraction
# Inheritance
# Polymorphism

# 01. Simple class example
class Emloyee:
    # These all are called class attributes like name email salary depart
    name = "Mohammad Ikram Khan"
    depart = "IT"
    email = 'abc@gmail.com'
    salary = 90000


emp = Emloyee()  # here emp is an object
print(emp.name, emp.depart, emp.salary)

# Add new attributes as age
emp.age = 36  # Here age is object or instance attribute not a class attribute
print(emp.name, emp.age, emp.depart, emp.salary)

# Update the class attributes
emp.name = "Meesum Ali"
print(emp.name, emp.age, emp.depart, emp.salary)

# =========== SELF PARAMETER ============

# 02 Example


class Car:
    def start_engine(self):
        print("Engine started")

    def drive(self):
        print("Car is driving")


my_car = Car()
my_car.start_engine()
my_car.drive()


# 03 Example
class Dog():
    name = 'bulldog'

    def bark(self):
        print("Woof Woof")


dog1 = Dog()
dog1.bark()

dog2 = Dog()
dog2.bark()
print(dog2.name)
