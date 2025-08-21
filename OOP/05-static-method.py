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
