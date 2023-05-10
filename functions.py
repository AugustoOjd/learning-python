def hello(name):
    print(f'hello {name}')

hello('jose gomez')

def add(name, lastName):
    return name + ' ' + lastName

print(add('jose', 'lopez'))

suma = lambda number1, number2: number1 + number2

print(suma(5, 4))