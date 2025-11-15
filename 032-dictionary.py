# The dictionary stores the data with key and value.

# Simple example of dictionary using f string format.

player = {'person': 'Ikram', 'coin': 45}
print(f'{player.person} has {player.coin} coin')


student = {
    "name": "Ikram",
    "email": 'ikram@gmail.com',
    'age': 39,
    'address': 'Korangi Karachi'
}

# Other way to print only one key
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

# Other way for get specific value of dictionery
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

# Sum of dictionary values
my_dict = {
    'a': 10,
    'b': 20,
    'c': 30,
    'd': 40,
    'e': 50
}
# Initialize a variable to store the sum
total_sum = 0

# Iterate through the values of the dictionary and add them to the tota
for i in my_dict.values():
    total_sum += i
# Print the sum of all items in the dictionary
print("Sum of all items in the dictionary:", total_sum)


# Merge two dictionary using the update() method:
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict1.update(dict2)
# The merged dictionary is now in dict1
print("Merged Dictionary (using update()):", dict1)


# Dictionary sorted by keys
sample_dict = {'apple': 3, 'pineapple': 5,
               'banana': 1, 'dates': 4, 'cherry': 2}

sorted_dict_by_keys = dict(sorted(sample_dict.items()))
print('test', sorted_dict_by_keys)
