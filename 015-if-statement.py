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


# forth example
marks = 80
result = ""
if marks < 30:
    result = "Failed"
elif marks > 75:
    result = "Passed with distinction"
else:
    result = "Passed"

print(result)
