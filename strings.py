myStr = "hello man"

# print(dir(myStr))

print(myStr.upper())

print(myStr.lower())

# print(myStr.swapcase())

print(myStr.capitalize())

change = myStr.replace('man', 'woman')

print(change)

# count characters
print(change.count('o'))

print(change.split('l'))

# find

print(change.find("a"))

#length

print(len(change))

# indice

# change.isnumeric()
# change.isalpha()

print(change[4])

# funcional string

print(f"saludos a {change}")
print("saludos a {0}".format(myStr))