# The input() function in Python is a built-in function used to obtain user input from
# the console. It pauses the program execution, displays a prompt message to the user,
# and waits for the user to type a response and press Enter.


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
price = float(input("Price of a rose?: "))
print(price)
