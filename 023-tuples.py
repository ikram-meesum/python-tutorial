# A tuple looks like a list, you use parentheses instead of square brackets.
# Once you define a tuple, you can access elements by using each item’s index.
# Tuples values cannot change is called immutable.

# Number tuples
dimensions = (20, 50)

print(dimensions[0])
print(dimensions[1])

# Error because it can not be change
# dimensions[0] = 250

# Tuples using loop
for dimension in dimensions:
    print(dimension)
