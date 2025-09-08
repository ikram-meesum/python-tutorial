# JSON is a syntax for storing and exchanging data.
# JSON is text, written with JavaScript object notation.

import json

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))


# 02 Example some JSON data:
x = '{ "name":"Ahmed Ali", "age":36, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])


# 03 Example a python object (dict):
x = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)


# 04 Example
a = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann", "Billy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}

print(json.dumps(a))

# The example above prints a JSON string, but it is not very easy to read, with no
# indentations and line breaks.

# Use the indent parameter to define the numbers of indents:
print(json.dumps(a, indent=4))

# Use the sort_keys parameter to specify if the result should be sorted.
json.dumps(a, indent=4, sort_keys=True)
