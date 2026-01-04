n = 9
for i in range(n):
    for j in range(i + 1):
        print('*', end='')
    print()

# Second example

n = 9
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print("*", end="")
    print("")
