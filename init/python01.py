# nombre = "ramon"
# cortado = nombre

# ingresar = int(input("agrega un nombre: "))
# mayuscula = ingresar


# tipado = type(mayuscula)

# print(tipado)
# print(mayuscula)

# operador1= 7
# operador2= 4

# condicionales

# edad = 3
# edad += 4
# valores = "estas loco"

# if 5 > 0:
#     print(edad)
# elif 5 > 2:
#     print("elif")
# else:
#     print(valores)

# listas

# letras = ["a", "b", "c"]
# letras.append("d")
# letras.insert(0, "inicio")
# letras.remove('inicio')

# letras[2] = "cc"

# print( letras )

# metodos importantes de las listas

# tuples

# letras = ('a', 'b', 'c', 'd', 'a', 'c')
# # 's' in letras

# print(letras.count('a'))

# diccionary

# edades = { 'gino': 15, 'nora': 45}
# edades['jose'] = 32
# del edades['nora']

# print(edades)

# ciclos y bucles

# nombre = 'maria'
# for i in range(2):
#     print(i)

# lista = [1, 2 ,3 ,4]

# for char in lista:
#     print(char * 2)

# letras = { "a": 12, "b": 5}

# for key, value in letras.items():
#     print(key, value)

# for claves in letras.values():
#     print(claves)

# while

# x = 20
# while x < 35:
#     print(x)
#     x += 3

# funciones

# def suma_basic():
#     print(1 + 2)

# suma_basic()

# def get_name(name, lastname):

#     print(name + lastname)

# get_name('jose ', 'lopez')

# def resta( x, y):
#     return  x - y

# resultado = resta(5, 6)
# print(resultado)

# funcion fibonacci

# def fib(n):
#     if n == 0 or n == 1:
#         return n
#     else:
#         return fib(n - 1) + fib(n-2)

# resultado = fib(3)
# print(resultado)

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)

# resultado = factorial(5)
# print(resultado)

#archivos ----

# notas = { 
#     "nora": 60,
#     "gino": 23,
#     "lorena": 42,
#     "talina": 31
# }

# nuevas_notas = {
#     "manuel": 60,
#     "ramon": 72
# }

# with open("data_estudiante.txt", "a") as archivo:
#     for i, nota in nuevas_notas.items():
#         archivo.write(i + " - " + str(nota) + "\n")


# try catch

num1= int(input('ingresa un numero'))
num2= int(input('ingresa un otro numero numero'))

try:
    resultado = num1 / num2
    print(f"{num1} / {num2} = ", resultado)
except:
    print('alerta pendiente')