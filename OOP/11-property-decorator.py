class Student():

    def __init__(self, chem, phys, math):
        self.chem = chem
        self.phys = phys
        self.math = math

    @property
    def percentage(self):
        return str((self.chem+self.phys + self.math) / 3) + "%"


s1 = Student(98, 90, 85)
print(s1.percentage)

s1.phys = 72
print(s1.percentage)
