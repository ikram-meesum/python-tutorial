# input function
myname = input("Please enter your name: ")
print("Hi", myname, "Developer")

# second example using split values
x, y = input("Enter two values: ").split()
print("Number of first value: ", x)
print("Number of second value: ", y)

# Typecasting string to integer
n = int(input("How many roses?: "))
print(n)

# Convert into float
price = float(input("Price of each rose?: "))
print(price)
