# Python variables are simply containers for storing data values.

# Simple print variable with single value
a = 9
print(a)

# Sum of two variable values
a = 4
b = 5
print(a + b)

# Result in 1 variable
a = 4
b = 5
c = a + b
print(c)

# String variable and integer variable both
name = "Ikram"
age = 36
print("My name is", name, 'and i am', age, "year old")


# Single line multiple variable assignment
a, b, c = 23, 54, 18
print(a, b, c)

# ====== CONSTANT =======
FILE_SIZE_LIMIT = 2000
print(FILE_SIZE_LIMIT)

# Reference
string1 = "Hello"
string2 = string1
string1 = "World"
print(string2)

# Calculate the area
length = float(input("What is length: "))
width = float(input("What is yor width: "))

area = length * width
print(f"The area is {area} cm")


# Swap values of 2 variable
j = 45
k = 50

j, k = k, j
print("j = ", j)
print("k = ", k)


# Swap multiple variable data type in single lines with values
x, y, z = 18, 27.5, "Python"
print(x, y, z)
