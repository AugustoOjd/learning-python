from random import choice


def jugar():
    usuario = input('Escoge una opcion: "pi" para piedra, "pa" para papel "ti" para tijera. \n ').lower()
    computadora = choice([ 'pi', 'pa', 'ti' ])

    if(usuario == computadora):
        return 'Empate!'

    if gano_el_jugador(usuario, computadora):
        return f'Ganaste! la pc eligio {computadora}'
    
    return f'Perdiste la pc eligio {computadora}'


def gano_el_jugador(jugador, oponente):

    if( (jugador == 'pi' and oponente == 'ti') or (jugador == 'ti' and oponente == 'pa') or (jugador == 'pa' and oponente == 'pi') ):
        return True
    else:
        return False


print(jugar())