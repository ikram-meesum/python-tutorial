# In Python, the try-except block is a fundamental used for handling exceptions,
# which are errors that occur during the execution of a program. This mechanism allows for
# graceful error management, preventing program crashes and enabling the application to
# continue running.

# try block:
# This block contains the code that is anticipated to raise an exception.

# except block(s):
# These blocks follow the try block and specify how to handle particular types of
# exceptions. If an exception occurs within the try block, Python jumps to the
# except block to execute the error-handling code.

# else block (optional):
# This block executes only if no exception is raised within the try block. It is useful
# for code that should only run when the try block completes successfully.

# finally block (optional):
# This block executes regardless of whether an exception occurred or not. It is typically
# used for cleanup operations, such as closing files.

# Zero division error
# Type error
# File error
# Sytext error
# Name error
# Index error


# 01 Example
print(x)
print("An exception occurred")

# 02 Example
try:
    print(x)
except:
    print("An exception occurred")

# 03 Example
# You can define as many exception blocks as you want, e.g. if you want to execute a
# special block of code for a special kind of error:

try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")

# 04 Example
# You can use the else keyword to define a block of code to be executed if no errors
# were raised:

try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")


# 05 Example
# The finally block will be executed regardless if the try block raises an error or not.
try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("The 'try except' is finished")

# Divided by zero
num1 = 12
num2 = 0
try:
    ans = num1/num2
except ZeroDivisionError:
    print('A number can not be divided by zero')
else:
    print('Answer:', ans)

# Index error
num1 = 5
num2 = 0
myList = [num1, num2]
try:
    ans = num1/num2
    print(myList[5])

except ZeroDivisionError:
    print('A number can not be divided by zero')
except IndexError:
    print(f"Your length is {len(myList)}")
else:
    print('Answer:', ans)


# Get all kind of errors
num1 = 5
num2 = 0
myList = [num1, num2]
try:
    ans = num1/num2
    print(myList[5])

# All exceptions are in exception class
except Exception as e:
    print(f"Error occured from above code: {e}.")
else:
    print('Answer:', ans)
