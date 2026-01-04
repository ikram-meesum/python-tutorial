import random

# Get random number using randint function
num = random.randint(1, 10)
print(num)

# Get random item using choise function
mylist = ["apple", "banana", "cherry"]
print(random.choice(mylist))

x = "WELCOME"
print(random.choice(x))

# Shuffle the item of list using shuffle function
fruit = ["apple", "banana", "cherry"]
random.shuffle(fruit)
print(fruit)

# Get 3 random item using sample function
mylist = ["apple", "banana", "cherry", "orange", "pine apple"]
print(random.sample(mylist, k=3))

# Return random number between 0.0 and 1.0:
print(random.random())

# Return a number between 3 and 9:
print(random.randrange(3, 9))
