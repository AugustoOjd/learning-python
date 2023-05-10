demoList = [1, 'hello', 1.42, True, [3,5,6]]
colors = ['red', 'green', 'blue']

nomberList = list((1, 2, 3, 4))
# print(nomberList)

# crea lista por parametros pasados antes del ultimo parametros
rangeList = list(range(1, 10))
# print(rangeList)

# print(dir(colors))
# print(len(colors))
# print(colors[1])

# includes in lista
print('green' in colors)

# replace with python
colors[0] = 'orange'
print(colors)

# push with python
colors.append('yellow')
# push by index
colors.insert(0, 'violet')
# push many str
colors.extend(['blanco', 'blanco', 'negro'])
# delete ultimo elemento or index
colors.pop()
colors.pop(0)
# delete by name
colors.remove('blue')
# vacia list
# colors.clear()

# order by, with reverse also
colors.sort()
# cuantas veces hay un elemento en lista
print(colors.count('blanco'))

print(colors)