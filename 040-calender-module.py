import calendar

year = int(input("Enter year: "))
month = int(input("Enter month: "))
print("")
calendar = calendar.month(year, month)
print(calendar)
