# Simple function define
def printMsg():
    print('Hi Developer')


printMsg()


# Function with one parameter
def printName(name):
    print(f'Hi {name} Developer')


printName()

# Function with two parameter


def printFullName(firstname, lastname):  # this is function parameter
    print(f'Hi {firstname} {lastname}.')


printFullName("Mohammad", "Ikram")  # this is function arguments

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


# Return a ditionery
def build_person(first_name, last_name):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    return person


fullname = build_person('Mohammad', 'Ikram')
print(fullname)

# Dislay data in dictionery key value pairs


def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile('Ahmed', 'Ali',
                             location='Karachi',
                             field='physics')
print(user_profile)
