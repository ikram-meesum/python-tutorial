# Simple print variable
a = 9
print(a)

# Two variable
a = 4
b = 5
print(a + b)

# Result in 1 variable
a = 4
b = 5
c = a + b
print(c)

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
