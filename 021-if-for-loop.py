# If condition in for loop

cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# Not Equat Operator
answer = 17
if answer != 42:
    print("That is not the correct answer.")


# Continue statement
for x in range(1, 15):
    if x == 9:
        continue
    else:
        print(x)

# Break statement
for x in range(1, 15):
    if x == 9:
        break
    else:
        print(x)

# Print item in one line using end
for x in range(1, 10):
    print(x, end=" ")

# Nested Loop
for x in range(3):
    for y in range(1, 10):
        print(y, end="")
    print()
