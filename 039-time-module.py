import time

time.sleep(3)
print("The End")
# --------------------------------------------

mytime = int(input("Enter the tiem in seconds: "))
for x in range(0, mytime):
    print(x)
    time.sleep(1)

print("Time is up")
