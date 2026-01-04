# r - Read
# a - Append
# w - Write
# x - Create / Add

# Read data from text file
f = open('029-names.txt')

# Print all names
print(f.read())

# Print only 6 character
print(f.read(6))

# Print one line
print(f.readline())

# Close the file
f.close()

# ===================
# Append data in file
f = open('029-names.txt', "a")
f.write('Testing123')
f.close()

f = open('029-names.txt')
print(f.read())
f.close()
# ---------------------

try:
    f = open('nofile.txt')
    print(f.read())
except:
    print('File does not exist.')
finally:
    f.close()


# Context Manager
# With keyword will open and close the file.
with open('file12.txt', 'r') as f:
    content = f.read()

print(content)

# Create file and write the content
with open('file3.txt', 'w') as f:
    f.write('Content write by python')
