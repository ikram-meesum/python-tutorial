# Print 0 to 9 using range function
for i in range(10):
    print(i)


# Start from 1 to 9
for i in range(1, 10):
    print(i)

# Start from 1 and increment by 2
for x in range(1, 10, 2):
    print(x)

# Information after end of loop
for x in range(6):
    print(x)
else:
    print("Finally finished!")

# loop on string value
for x in 'banana':
    print(x)

# Reverse the loop
for x in reversed(range(1, 11)):
    print(x)

# Create a list using list function
numbers = list(range(1, 6))
print(numbers)

# Square number of iterate number and submit it in empty list
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)


# Get the sum of loop
theSum = 0
for count in range(5):
    theSum += count

print(theSum)


# Reverse loop
for count in range(10, 0, -1):
    print(count, end=" ")

# increment in loop value
for count in range(5):
    print(count + 1, end=" ")
