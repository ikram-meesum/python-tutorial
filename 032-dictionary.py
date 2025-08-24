# The dictionary stores the key and value. The last
# two lines access and display that information, as shown here:

student = {
    "name": "Ikram",
    "email": 'ikram@gmail.com',
    'age': 39,
    'address': 'Korangi Karachi'
}

# Print only one key
print(student['name'])

# Get two key
print(f"My name is {student['name']} and email is {student['email']}")

# Print all key and value
print(student)

# Get data in list
print(student.items())

# Get keys only
print(student.keys())

# Get values only
print(student.values())

# Update or modify the specific key value
student.update({"name": "Mohammad Ikram Khan"})
print(student)

# Other type for get specific value of dictionery
print(student.get("email"))

# Get keys and values using loop
for key, value in student.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")


# Merg dictionery in one list
a = {'color': 'green', 'points': 5}
b = {'color': 'yellow', 'points': 10}
c = {'color': 'red', 'points': 15}

allDict = [a, b, c]

for f in allDict:
    print(f)

# Nested Dictionery
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")

# Delete a specific
