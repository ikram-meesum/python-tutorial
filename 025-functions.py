# Simple function define
def printName():
    print('Hi Developer')


printName()

# Function with parameter


def printFullName(firstname, lastname):
    print(f'Hi {firstname} {lastname}.')


printFullName("Mohammad", "Ikram")

# Function return statement


def doSum(num1, num2):
    return (num1+num2)


total = doSum(4, 5)
print(total)

# Scope in function
myname = "Ikram"


def printSimpleName():
    color = 'white'
    print(myname)


printSimpleName()
# print(color)  # Error of scope


def secondFunc():
    printSimpleName()


secondFunc()

# Multiple arguments


def multy(*numbers):
    print(numbers)


multy(3, 5, 9, 8)

# Default Argument


def showinfo(name, city="Hyderabad"):
    print("Name:", name)
    print("City:", city)
    return


# Now call showinfo function
showinfo(name="Arsh", city="Karachi")
showinfo(name="Haris")

showinfo("Ikram", "Lahore")
showinfo("Kamran")
