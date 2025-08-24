# loop on list element
fruits = ["apple", "banana", "cherry", "Mango", "orange"]
for x in fruits:
    print(x)

# Break loop using break keyword on specific condition
# fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)

print("-----------")
# Continue keyword use to skip the print
# fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

# Only colon means all element of list
f = fruits[:]
print("Same list", f)


# Nested for loop
color = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in color:
    for y in fruits:
        print("Nested List:", x, y)

# Nested List
groceries = [["apple", "banana", "orange", "coconut"], [
    "celery", "carrots", "potates"], ["chicken", "fish", "turkey"]]

for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()
