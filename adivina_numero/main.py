from random import randint


def adivina_el_numero(x):
    print('====================')
    print('Bienvenido al juego')
    print('====================')
    print('Tu meta es adivinar el numero que genera la computadora')

    numero_aleatorio = randint(1, x) # numero aleatorio entre 1 y x.

    prediction = 0

    while prediction != numero_aleatorio:
        prediction = int(input(f'Adivina un numero entre 1 y {x}: '))

        if prediction < numero_aleatorio:
            print('el numero es mayor al que ingresaste')
        if prediction > numero_aleatorio: 
            print('el numero es menor al que ingresaste')
    
    print(f'Felicitaciones el numero era {numero_aleatorio}')


adivina_el_numero(10)
