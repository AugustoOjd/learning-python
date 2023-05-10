from random import randint

def adivina_el_numero_pc(x):
    print('======================')
    print(' Bienvenido al juego')
    print('======================')
    print(f'Selecciona un numero entre 1 y {x} para que la computadora intente adivinar')

    limite_inferior = 1
    limite_superior = x

    respuesta = ''

    while respuesta != 'c':
        #generar una prediccion

        if(limite_inferior != limite_superior):
            prediction = randint(limite_inferior, limite_superior)
        else: 
            prediction = limite_inferior

        respuesta = input(f'Mi prediccion es {prediction}. Si es alta, ingresa (A). si es muy baja ingresa (B). si es correcto ingresa (C)').lower()
        
        if respuesta == "a":
            limite_superior = prediction - 1
        elif respuesta == "b":
            limite_inferior = prediction + 1
    
    print(f'Si, la computadora adivino el numero correctamente: {prediction}')

adivina_el_numero_pc(100)