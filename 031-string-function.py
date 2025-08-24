# Title Function use for first capital letter
name = "mohammad ikram khan"
print(name.title())

res = name.capitalize()
res = name.isdigit()
res = name.isalpha()
print(res)

# Upper and lower character case
name2 = "aHmed Ali"
print(name2.upper())
print(name2.lower())

# Remove blank spaces from right side
language = 'python '
print(len(language))
language = language.rstrip()
print(len(language))

# Remove blank spaces from left side
language = ' python '
print(len(language))
language = language.lstrip()
print(len(language))

# Remove blank spaces from both side
language = ' python '
print(len(language))
language = language.strip()
print(len(language))

# Find function
name = input("Yor name")
res = name.find("a")
print(res)

# Remove prefix from url
url = 'https://youtube.com'
print(url.removeprefix('https://'))

# Center function
title = "MENU"
print(title.center(20, '='))
print("Coffee".ljust(16, '.') + "$1".rjust(4))

# Count Function
phone = "1-234-567-890"
res1 = phone.count("-")
print(res1)

# Replace Function
res2 = phone.replace("-", " ")
print(res2)

# Some working with string
phone = "1234-5678-9012-3456"
print(phone[0])
print(phone[0:4])
print(phone[:4])
print(phone[4:])
print(phone[-1])
print(phone[::3])
print(phone[-4:])
print(phone[::-1])

# Working with decimal
price = 5.2345
print(f"price is {price:.2f}")
print(f"price is {price:10}")
print(f"price is {price:+}")
print(f"price is {price:,}")
print(f"price is {price:+,.2f}")
