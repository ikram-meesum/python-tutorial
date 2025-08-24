a = 5
b = 4

if int(a) < int(b):
    print(f"{a} is greater than {b}!")
else:
    print(f"{b} is less than {a}!")

#  second example

if "c" == "d":
    print("Value is equal")
else:
    print("Value is not equal")


# third example

if "c" == "C":
    print("Value is equal")
else:
    print("Value is not equal")

# forth exampl

age = int(input("enter yor age"))
if age >= 18:
    print("You ae now sign up")
else:
    print("yo are under 18")

# Other example
res = input("Wold yor like food? Y/N")
if res == "Y":
    print("Have some food")
else:
    print("No food for yo")

# Other example
forsale = True

if forsale:
    print("This item is for sale")
else:
    print("This item is not for sale")

# Other example
temp = 25
issunny = True

if temp >= 28 and issunny:
    print("It is hot and sunny")

# Other example
num = int(input("Enter your number"))
if num > 0:
    print("It is a positive number")
elif num == 0:
    print("It is zero")
else:
    print("It is a negtive number")
