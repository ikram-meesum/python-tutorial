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
