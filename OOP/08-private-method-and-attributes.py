class Student():
    __name = "Kamran Khan"

    def __greetting(self):
        print(f"Hi {self.__name} Developer.")

    def welcome(self):
        self.__greetting()


s1 = Student()
s1.welcome()
