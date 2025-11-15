# Even and odd number check
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("This is a even number")
else:
    print("This is a odd number")


# Simple example
num = float(input("Enter a number: "))
if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")


# second example
x = int(input("Please enter an integer: "))

if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')

# Other example
marks = 80
result = ""
if marks < 30:
    result = "Failed"
elif marks > 75:
    result = "Passed with distinction"
else:
    result = "Passed"

print(result)

# Other example
age = int(input("enter yor age"))
if age >= 18:
    print("You ae now sign up")
elif age < 0:
    print("You have not to been born")
elif age >= 100:
    print("Yo are too old")
else:
    print("yo are under 18")

# Othe condition with and operator
number = int(input("Enter the numeric grade: "))
if number > 0 and number <= 100:
    print('Value is between 1 and 100')
else:
    print("Error: grade must be between 100 and 1")


# Nested If Else Statement

account = input("Do you have a bank account? Y/N")
if account == "Y":
    atm = input("Do you have a valid /activated ATM Y/N")
    if atm == "Y":
        balance = input("Do you have sufficient balance in account? Y/N")
        if balance == "Y":
            pin = input("Have you entered a correct PIN code?")
            if pin == "Y":
                print("You can withdraw money from atm")
            else:
                print("You can not withdraw money from atm")
        else:
            print("You can not withdraw money from atm")
    else:
        print("You can not withdraw money from atm")
else:
    print("You can not withdraw money from bank")

# Nested If else

age = int(input("What is the age? "))
if age <= 22:
    qualification = input("What is the qualification?")
    if qualification == "graduate":
        complexion = input("Whats the complexion")
        if complexion == "fair":
            hair_length = float(input("Kitne feet bal hen"))
            if hair_length >= 2:
                height = float(input("Enter height in feet"))
                if height >= 5:
                    weight = float(input("Weight kitna hy?"))
                    if weight <= 60:
                        cooking = input("Khana pakan ata hy")
                        if cooking == "yes":
                            print("Interested! Mubarak ho!")
                        else:
                            print("Not interested")
                    else:
                        print("Not interested")

                else:
                    print("Not interested")

            else:
                print("Not interested")

        else:
            print("Not interested")

    else:
        print("Not interested")
else:
    print("Not interested")
