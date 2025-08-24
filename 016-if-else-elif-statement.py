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
