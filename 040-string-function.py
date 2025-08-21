# Title Function use for first capital letter
name = "mohammad ikram khan"
print(name.title())

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


# Remove prefix from url
url = 'https://youtube.com'
print(url.removeprefix('https://'))

# Center function
title = "MENU"
print(title.center(20, '='))
print("Coffee".ljust(16, '.') + "$1".rjust(4))
