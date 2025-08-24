# Simple while loop
i = 0
while i < 6:
    print(i)
    i += 1

# Second example
count = 1
while count < 5:
    print(f"Count is: {count}")
    count += 1
else:
    print("Loop finished normally.")

# Break statement using while loop
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

# Continue statement
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

# Other example
food = input("Enter a food your lik (q to quit): ")
while not food == "q":
    print(f"You like {food}")
    food = input("Enter another food you like (q to quit): ")
print("Bye")

# Other example
name = input("Your name is: ")
while name == "":
    print("You did not enter name")
    name = input("Your name is: ")
print(f"Hi {name}")

# Other example
num = int(input("Enter a # between 1-10: "))
while num < 1 or num > 10:
    print(f"{num} is not valid")
    num = int(input("Enter a # between 1-10: "))
print(f"Your number is {num}")

# Delete specific item in a list
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)
