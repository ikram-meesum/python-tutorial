# Python offers various types of operators to perform different operations. Here are
# examples of common operator types:

# =============== 01 - Arithmetic Operators: Used for mathematical calculations. ==========

a = 4
b = 5

print(f"Addition: {a + b}")       # Output: Addition: 13
print(f"Subtraction: {a - b}")    # Output: Subtraction: 7
print(f"Multiplication: {a * b}")  # Output: Multiplication: 30
print(f"Division: {a / b}")       # Output: Division: 3.3333333333333335
print(f"Floor Division: {a // b}")  # Output: Floor Division: 3
print(f"Modulus: {a % b}")        # Output: Modulus: 1
print(f"Exponentiation: {a ** b}")  # Output: Exponentiation: 1000

# ================ 02 - Comparison Operators: Used to compare two values. ===============

x = 5
y = 8

print(f"Equal: {x == y}")        # Output: Equal: False
print(f"Not Equal: {x != y}")     # Output: Not Equal: True
print(f"Greater Than: {x > y}")   # Output: Greater Than: False
print(f"Less Than: {x < y}")      # Output: Less Than: True
print(f"Greater or Equal: {x >= y}")  # Output: Greater or Equal: False
print(f"Less or Equal: {x <= y}")  # Output: Less or Equal: True

# ================ 03 - Assignment Operators: Used to assign values to variables ===========
a = 10
b = a
print(b)

b += a  # Equal to b = a + a
print(b)

b -= a  # Equal to b = a - a
print(b)

b *= a  # Equal to b = a * a
print(b)

# Other example
friends = 5
friends = friends + 1
friends += 1
friends = friends ** 2
remainder = friends % 3
print(remainder)

# Other example
print("." * 10 + "Python")


# Other Example
num = 10

num += 5  # Equivalent to num = num + 5
print(f"Addition Assignment: {num}")  # Output: Addition Assignment: 15

num -= 2  # Equivalent to num = num - 2
print(f"Subtraction Assignment: {num}")  # Output: Subtraction Assignment: 13

num *= 3  # Equivalent to num = num * 3

# Output: Multiplication Assignment: 39
print(f"Multiplication Assignment: {num}")

# ================= 04 - Logical Operators: Used to combine conditional statements. ========
a = True
b = False

print(a and b)  # Both value or condition should be true then answer will be true
print(a or b)  # Any one value or condition should be true then answer will be true
print(not a)  # Opposit value or condition like true to false or false to true

# Other example

p = True
q = False

print(f"AND: {p and q}")  # Output: AND: False
print(f"OR: {p or q}")   # Output: OR: True
print(f"NOT: {not p}")   # Output: NOT: False

# Second example
x = 5
y = 10

# Output: True (both are true)
print(f"and (x < 10 and y > 5): {x < 10 and y > 5}")

# Output: True (at least one is true)
print(f"or (x > 10 or y > 5): {x > 10 or y > 5}")

# Output: True (reverses the result)
print(f"not (x > 10): {not (x > 10)}")


# ============== 05 - Membership Operators: Used to test if a sequence contains a value =====

# In operator
print('s' in 'ikram')

# Example 02

character = input("Enter a character? ")
vowels = 'aeiou'
if character in vowels:
    print("Vowel")
else:
    print('consonant')

# Example 03

my_list = [1, 2, 3, 4, 5]
print(f"Is 3 in list?: {3 in my_list}")      # Output: Is 3 in list?: True

# Output: Is 6 not in list?: True
print(f"Is 6 not in list?: {6 not in my_list}")

# ============== 06 - Identity Operators: Used to compare the memory locations of two objects. ===========

a = 10
b = 20
c = a

print(a is not b)
print(a is c)

# Othe example

list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

# Output: list1 is list2?: False (different memory locations)
print(f"list1 is list2?: {list1 is list2}")

# Output: list1 is list3?: True (same memory location)
print(f"list1 is list3?: {list1 is list3}")


# ============= 07 -  Membership Operators ========================
# Used to test whether a value is present in a sequence (like a list, tuple, or string)

fruits = ["apple", "banana", "cherry"]

print(f"'banana' in fruits: {'banana' in fruits}")     # Output: True
print(f"'grape' in fruits: {'grape' in fruits}")       # Output: False
print(f"'mango' not in fruits: {'mango' not in fruits}")  # Output: True

# =============== 08 - Ternary Operator =================

a, b = 10, 20
print(f"a is {a} and b is {b}")

min = a if a < b else b
print(f"{min} is min value.")

# Second Example
num = 8
print('Yes') if num > 10 else print('No')

# Other example
print("Positive" if num > 0 else "Negative")
print("Even" if num % 2 == 0 else "Odd")
