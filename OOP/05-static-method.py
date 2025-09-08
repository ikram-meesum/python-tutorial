class Student():
    # constructor
    def __init__(self, fullname, myage):
        self.name = fullname
        self.age = myage

    @staticmethod  # decorator (its mean without self)
    def greetting():
        print("Hi developer")


s1 = Student("Ahmed Ali", 36)
s1.greetting()


# Other example regarding static method
class Bike:
    color = 'Black'
    modal = 2025
    name = 'Honda'

    def start_engine(self):
        print("Engine started")

    @staticmethod  # This will ignore the error and allow for execution
    def greet():  # This will produce an error regarding self parameter
        print("Car is driving")

    def info(self):
        print(
            f"Bike name is {self.name} and color is {self.color} of modal {self.modal}")


my_bike = Bike()
my_bike.start_engine()
my_bike.greet()
my_bike.info()
