from palabras import palabras
from random import choice
from ahorcado_diagrama import vidas_diccionario_visual
import string

def obtener_palabra_valida(palabra):
    #selecionar palabra aleatora de la lista
    palabra = choice(palabras)

    while '-' in palabra or ' ' in palabra:
        palabra = choice(palabras)

    return palabra.upper()

def ahorcado():
    print('--- Bienvenido ---')

    palabra = obtener_palabra_valida(palabras)

    letras_por_adivinar = set(palabra)
    letras_adivinadas = set() #No {}
    abecedario = set(string.ascii_uppercase)

    vidas = 7

    while len(letras_por_adivinar) > 0 and vidas > 0:
        #letras adivinadas 
        #' '.join({ 'a', 'b', 'c'}) = 'a b c'
        print(f'Te quedan {vidas} vidas y has usando estas letras: {" ".join(letras_adivinadas)}')

        # Mostrar el estado actuald el la palabra
        palabra_lista = [ letra if letra in letras_adivinadas else '-' for letra in palabra]
        print(vidas_diccionario_visual[vidas])
        print(f'Palabra: {" ".join(palabra_lista)}')

        letra_usuario = input('Escoge una letra: ').upper()
        
        if( letra_usuario in abecedario - letras_adivinadas):
            letras_adivinadas.add(letra_usuario)


            if(letra_usuario in letras_por_adivinar):
                letras_por_adivinar.remove(letra_usuario)
                print('')
            else:
                #or vidas = vidas - 1
                vidas -= 1
                print(f'\n Tu letra, {letra_usuario} no esta en la palabra')
        elif letra_usuario in letras_adivinadas:
            print('\n ya selecionaste esa letra anteriormenete, elige otra letra')
        else:
            print('Esta letra no es valida')
    
    # El juego llega a esta linea cuando se cumple algun requisito del while

    if vidas == 0:
        print(vidas_diccionario_visual[vidas])
        print(f'Perdiste, la palabra era: {palabra}')

    else:
        print(f'Ganaste!! Adivinistaste la palabra {palabra}')

ahorcado()
