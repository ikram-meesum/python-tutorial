# Upper case the first letter in this sentence:
txt = "hello, and welcome to my world."
x = txt.capitalize()
print(x)

# Make the string lower case:
txt = "Hello, And Welcome To My World!"
x = txt.casefold()
print(x)

# Print the word "banana", taking up the space of 20 characters, with "banana" in the middle:
txt = "banana"
x = txt.center(20)
print(x)

# The center() method will center align the string, using a specified character
# (space is default) as the fill character.

# Other example
txt = "banana"
x = txt.center(20, "-")
print(x)

# Return the number of times the value "apple" appears in the string:

txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x)


# string.count(value, start, end)
# The position to start the search. Default is 0

txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple", 10, 24)
print(x)


# Check if the string ends with a punctuation sign (.):
txt = "Hello, welcome to my world."
x = txt.endswith(".")
print(x)

# Other example
txt = "Hello, welcome to my world."
x = txt.endswith("my world.")
print(x)


# Where in the text is the word "welcome"?:
txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x)


# Where in the text is the first occurrence of the letter "e"?:
txt = "Hello, welcome to my world."
x = txt.find("e")
print(x)


# Where in the text is the first occurrence of the letter "e" when you only search
# between position 5 and 10?:
# If the value is not found, the find() method returns -1,

txt = "Hello, welcome to my world."
x = txt.find("e", 5, 10)
print(x)


# Insert the price inside the placeholder, the price should be in fixed point,
# two-decimal format:

txt = "For only {price:.2f} dollars!"
print(txt.format(price=49))

# Using different placeholder values:
txt1 = "My name is {fname}, I'm {age}".format(fname="John", age=36)
txt2 = "My name is {0}, I'm {1}".format("John", 36)
txt3 = "My name is {}, I'm {}".format("John", 36)


# The index() method finds the first occurrence of the specified value.
txt = "Hello, welcome to my world."
x = txt.index("welcome")
print(x)


#  Where in the text is the first occurrence of the letter "e"?
txt = "Hello, welcome to my world."
x = txt.index("e")
print(x)


# Where in the text is the first occurrence of the letter "e" when you only search
# between position 5 and 10?:

txt = "Hello, welcome to my world."
x = txt.index("e", 5, 10)
print(x)

# Check if all the characters in the text are alphanumeric:
txt = "Company12"
x = txt.isalnum()
print(x)

# Check if all the characters in the text is alphanumeric:
txt = "Company 12"
x = txt.isalnum()
print(x)


# Check if all the characters in the text are letters:
txt = "CompanyX"
x = txt.isalpha()
print(x)


# Check if all the characters in the text are digits:
# The isdigit() method returns True if all the characters are digits, otherwise False.

txt = "50800"
x = txt.isdigit()
print(x)


# Check if all the characters in the text are in lower case:

txt = "hello world!"
x = txt.islower()
print(x)

# Other example
a = "Hello world!"
b = "hello 123"
c = "mynameisPeter"

print(a.islower())
print(b.islower())
print(c.islower())

# Check if each word start with an upper case letter:
# The istitle() method returns True if all words in a text start with a upper case
# letter, AND the rest of the word are lower case letters, otherwise False.

txt = "Hello, And Welcome To My World!"
x = txt.istitle()
print(x)

# Check if all the characters in the text are in upper case:
# The isupper() method returns True if all the characters are in upper case,
# otherwise False.
# Numbers, symbols and spaces are not checked, only alphabet characters.

txt = "THIS IS NOW!"
x = txt.isupper()
print(x)

# The join() method takes all items in an iterable and joins them into one string.
# A string must be specified as the separator.
# Join all items in a tuple into a string, using a hash character as separator:

myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x)

# Join all items in a dictionary into a string, using the word "TEST" as separator:

myDict = {"name": "John", "country": "Norway"}
mySeparator = "TEST"
x = mySeparator.join(myDict)
print(x)


# Return a 20 characters long, left justified version of the word "banana":
# The ljust() method will left align the string, using a specified character
# (space is default) as the fill character.

txt = "banana"
x = txt.ljust(20)
print(x, "is my favorite fruit.")


txt = "banana"
x = txt.ljust(20, "O")
print(x)


# The lower() method returns a string where all characters are lower case.

txt = "Hello my FRIENDS"
x = txt.lower()
print(x)


# Remove spaces to the left of the string:
# The lstrip() method removes any leading characters (space is the default leading
# character to remove)

txt = "     banana     "
x = txt.lstrip()
print("of all fruits", x, "is my favorite")

# Remove the leading characters:

txt = ",,,,,ssaaww.....banana"
x = txt.lstrip(",.asw")
print(x)


# The replace() method replaces a specified phrase with another specified phrase.
# Replace the word "bananas":

txt = "I like bananas"
x = txt.replace("bananas", "apples")
print(x)


# Replace the two first occurrence of the word "one":
txt = "one one was a race horse, two two was one too."
x = txt.replace("one", "three", 2)
print(x)

# Where in the text is the last occurrence of the string "casa"?:
txt = "Mi casa, su casa."
x = txt.rfind("casa")
print(x)

# The rfind() method finds the last occurrence of the specified value.
# The rfind() method returns -1 if the value is not found.
# The rfind() method is almost the same as the rindex() method. See example below.

# Where in the text is the last occurrence of the letter "e" when you only search between position 5 and 10?:

txt = "Hello, welcome to my world."
x = txt.rfind("e", 5, 10)
print(x)


# The rindex() method finds the last occurrence of the specified value.
# The rindex() method raises an exception if the value is not found.
# The rindex() method is almost the same as the rfind() method. See example below.

txt = "Mi casa, su casa."
x = txt.rindex("casa")
print(x)

# Where in the text is the last occurrence of the letter "e" when you only search between
# position 5 and 10?:
# If the value is not found, the rfind() method returns -1,

txt = "Hello, welcome to my world."
x = txt.rindex("e", 5, 10)
print(x)

# Return a 20 characters long, right justified version of the word "banana":
txt = "banana"
x = txt.rjust(20)
print(x, "is my favorite fruit.")

# Second Example
txt = "banana"
x = txt.rjust(20, "O")
print(x)

# The rsplit() method splits a string into a list, starting from the right.
# Split a string into a list, using comma, followed by a space (, ) as the separator:
txt = "apple, banana, cherry"
x = txt.rsplit(", ")
print(x)

# Remove any white spaces at the end of the string:
txt = "     banana     "
x = txt.rstrip()
print("of all fruits", x, "is my favorite")

# The split() method splits a string into a list.
# Split a string into a list where each word is a list item:
txt = "welcome to the jungle"
x = txt.split()
print(x)

# Othe example
txt = "hello, my name is Peter, I am 26 years old"
x = txt.split(", ")
print(x)

# Othe example
txt = "hello, my name is Peter, I am 26 years old"
x = txt.split("e")
print(x)

# Third example
txt = "apple#banana#cherry#orange"
x = txt.split("#")
print(x)

# Forth example
txt = "apple#banana#cherry#orange"
# setting the maxsplit parameter to 1, will return a list with 2 elements!
x = txt.split("#", 1)
print(x)


# The startswith() method returns True if the string starts with the specified
# value, otherwise False.
# Check if the string starts with "Hello"

txt = "Hello, welcome to my world."
x = txt.startswith("Hello")
print(x)

# Other example
txt = "Hello, welcome to my world."
x = txt.startswith("wel", 7, 20)
print(x)


# Check if the string starts with either "Hello" or "Hi":
txt = "Hi, welcome to my world."
x = txt.startswith(("Hello", "Hi"))
print(x)

# Remove spaces at the beginning and at the end of the string:
txt = "     banana     "
x = txt.strip()
print("of all fruits", x, "is my favorite")


# Remove the leading characters:
txt = ",,,,,rrttgg.....banana....rrr"
x = txt.strip(",.grt")
print(x)


# Make the lower case letters upper case and the upper case letters lower case:
txt = "Hello My Name Is PETER"
x = txt.swapcase()
print(x)

# The title() method returns a string where the first character in every word is
# upper case. Like a header, or a title.
# Make the first letter in each word upper case:

txt = "Welcome to my world"
x = txt.title()
print(x)


# The zfill() method adds zeros (0) at the beginning of the string, until it reaches
# the specified length.
# Fill the string with zeros until it is 10 characters long:
txt = "50"
x = txt.zfill(10)
print(x)


# ==================================================

text = input("Enter some text here: ").lower()
vowels = 'aeiou'
count_a = text.count('a')
count_e = text.count('e')
count_i = text.count('i')
count_o = text.count('o')
count_u = text.count('u')
total = count_a+count_e+count_i+count_o+count_u
total
