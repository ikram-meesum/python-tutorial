class Student():
    # constructor
    def __init__(self, fullname):
        self.name = fullname
        print("getting student record")


s1 = Student("Ahmed Ali")
print(s1.name)
