class Student():

    # Using double underscore make private arribute
    __myname = "Ahmed Ali"

    # Using double underscore make private method
    def __greeting():
        print("Hi from student class")


s1 = Student()
print(s1.__myname)
# It can not access from here it access only in the class
s1.__greeting()
