# Useless without loop or list function
# numbers = range(1, 6)

# List function creates a array list. It use only for number range
numbers = list(range(1, 6))
print(numbers)

# Create even number
even_numbers = list(range(2, 11, 2))
print(even_numbers)


squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)
