# 1. A tuple looks like a list, you use parentheses instead of square brackets.
# 2. Once you define a tuple, you can access elements by using each item’s index.
# 3. Tuples values cannot change is called immutable.
# 4. Tuple has 02 method count and index only


# Number tuples
dimensions = (20, 50)

print(dimensions[0])
print(dimensions[1])

# Error because it can not be change
# dimensions[0] = 250

# Tuples using loop
for dimension in dimensions:
    print(dimension)

# Get items by range
fruit = ("apple", "banana", "cake", "orange")
print(fruit[1:4])

# Second way of create tuple
a = tuple([1, 2, 3, 4, 5])
print(type(a))

# Third way of create tuple
b = (9,)
print(type(b))

# Forth way of create a tuple
c = 'ikram', 45
print(type(c))

# Check item exist
colors = ('red', 'white', "black", "green")
print("yellow" in colors)
