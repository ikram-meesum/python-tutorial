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

# Other example
age = int(input("Enter age"))
if (age >= 13) and (age <= 19):
    print("Teenager")
else:
    print("Not Teenager")


# age  = int(input("Apni umer bataen: "))
if age >= 60:
    print("Senior Citizen")
elif age >= 40:
    print("Adult")
elif age >= 20:
    print("Young")
elif age >= 13:
    print("Teenager")
elif age >= 2:
    print("Kid")
else:
    print("Toddler")

# Tax calculator
total = int(input("Enter amount"))
discount = None
if total >= 50000:
    discount = total * 0.15
elif total >= 30000:
    discount = total * 0.10
elif total >= 15000:
    discount = total * 0.075
elif total >= 10000:
    discount = total * 0.05
else:
    discount = total * 0
print(f"Your total amount is {total}")
print(f"Your discount is Rs: {discount}")
print(f"Your payable amount is {total - discount}")


# Get Percentage

python = int(input("Enter python marks"))
stats = int(input("Enter stats marks"))
ml = int(input("Enter ML marks"))
ai = int(input("Ener AI marks"))
project = int((input("Ener project marks")))
total = python+stats+ml+ai+project
percentage = total/500*100
grade = None
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"
print(f"You have total {total} marks out of 500")
print(f"Your percentage is {percentage}")
print(f"Your grade is {grade}")


# Check even and odd number

num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is even")
