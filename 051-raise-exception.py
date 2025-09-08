# In Python, the raise keyword is used to explicitly trigger an exception. This allows
# programmers to signal the occurrence of an error or an exceptional condition that
# prevents the normal execution flow of a program.


# Raise an error and stop the program if x is lower than 0:

# 01 Example
x = -1

if x < 0:
    raise Exception("Sorry, no numbers below zero")

# 02 Example
x = "hello"

if not type(x) is int:
    raise TypeError("Only integers are allowed")
