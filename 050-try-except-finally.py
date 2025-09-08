# In Python, the try-except block is a fundamental construct used for handling exceptions,
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
