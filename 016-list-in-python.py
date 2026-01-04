# A list in Python is a built-in, ordered, and mutable (changeable) collection of items,
# enclosed in square brackets []. Lists allow duplicate values, can contain mixed data
# types (integers, strings, booleans, etc.), and zero-indexed, meaning the first item
# is at index 0.

# Empty list
a = []
print(len(a))

# list with int values
a = [1, 2, 3]
print(a)

# list with mixed int and string
b = ["Google", "Facebook", "Microsoft", 14, 45]
print(b)

print(b[0].lower())  # Get first element
print(b[2])  # Get third element

print("Accessing element using negative indexing")
print(b[-1])  # Get last index
print(b[-3])  # Get third index from last

# Update the item in the list
b[1] = "Youtube"
print(b)

# Append function use for add item in list at the end
b.append("Twitter")

print(f"Value of b is: {b}")

# Get specific range value
print(f"Value from 1 to 3: {b[1:3]}")

# Get value from start to till 3 of list
print(f"Value from 3 to end of list: {b[:3]}")

# Get value start from 2 index element of list
print(f"Value start from 2 index element: {b[2:]}")


# Get last 3 element of list
print(f"Last 3 element: {b[-3:]}")


# Add item in blank list
car = []
car.append("Honda")
car.append("Toyota")
car.append("KIA")
car.append("Suzuki")
print(car)

# Insert element in list at any position
car.insert(0, "Audi")
print(car)

# Delete element from list using del keyword
del car[2]
print(car)

# Remove element form last using pop function if no parameter value and return a value
p = car.pop()
print(f"Deleted element: {p}")
print(car)

# Remove specific element using pop function parameter value
p = car.pop(1)
print(f"Second deleted element: {p}")
print(car)

# Remove element by item name
car.remove('KIA')
print(car)

# Sort element by sort function accending order
city = ["Karachi", "Lahore", "Islamabad", "Quetta", "Peshawar"]
city.sort()
print(city)

# Sort element by sort function decending order
city = ["Karachi", "Lahore", "Islamabad", "Quetta", "Peshawar"]
city.sort(reverse=True)
print(city)

# Reverse order list not accending or decending order
fruit = ["Banana", "Orange", "Strawberry", "Mango", "Pinapple"]
print('---- BEFORE -----')
print(fruit)
print('---- AFTER -----')
fruit.reverse()
print(fruit)

# Count list element
print(len(fruit))

# Working with list
fruits = ["apple", "banana", "cake", "orange", "pine apple", "strawberry"]
# Get first 2 element or item
print(fruits[0:2])

# Get first 2 element or item
print(fruits[:2])

# Get item from index 2 to end
print(fruits[2:])

# Get item from start to end with 1 skip
print(fruits[::2])

# Get last one item
print(fruits[-1:])

# Get from -3 to last indexing
print(fruits[-3:])

# Get from start to end item
print(fruits[::])

# Reverse all item in decending order
print(fruits[::-1])

#
print(fruits[-4:-1])

#
print(fruits[-1:-4:-1])


# Empty List will be return because invalid indexing start to end
print(fruits[3:1])

# Loop on list
for x in fruits:
    print(x)
# Count list items
print(len(fruits))
# Check item already exist
print("banana" in fruits)

# Update an item

fruits[0] = "pinapple"

for x in fruits:
    print(x)

# Empty List
fruits.clear()

# Find a Index of item
fruits.index("apple")

# Count specific item
fruits.count("banana")  # count the qty

# Copy a list
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

# friend_foods = my_foods
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)


# Concatenate 2 list
lstA = [1, 3, 5, 7, 9]
lstB = [2, 4, 6, 8, 10]

lstC = lstA + lstB
print(lstC)


# Remove range items

grocery = ['kecthup', 'atta', 'rice', 'sugar', 'milk',
           'shanmasala', 'oil', 'mirchen', 'namak', 'ghee']

del grocery[2:5]


# Merge 2 list
employee = ['Mohib', 'Rehan', 'Sohaib', 'Zesshan']
old_emloyee = ['Aslam', 'Jahazaib', 'Kashif']

employee.extend(old_emloyee)
print(employee)


# Copy a list into new empty list
emp = ["Ikram", "Akram", "Islam"]
new_emp = emp.copy()
print(new_emp)

# Nested List
a = [20, [30, 40, [50, "develope", 70]], 90]
print(a[1][2][1])

#
students = ["Ikram", "Kaleem", "Amir", "Yaseen", "Usman"]
for std in students:
    print(f"Mr {std} please join online class for today")

#
for std in students:
    if std == "Amir":
        print(f"Mr {std}, Kal off nahi hay!")
    else:
        print(f"Mr {std}, Kal off hay!")

#
for std in students:
    if std.count("e") >= 2:
        print(f"Mr {std}, Kal off nahi hay!")
    else:
        print(f"Mr {std}, Kal off hay!")

# Get Max and Min value in a list
lst3 = [34, 54, 67, 90]

# Max value is
print(f"The max value is: {max(lst3)}")

# Min value is
print(f"The min value is : {min(lst3)}")
