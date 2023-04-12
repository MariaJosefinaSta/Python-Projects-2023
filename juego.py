# Importar librería deque, importa una cola que sirve para rotar el turno del jugador
from collections import deque

turno = deque(["0", "x"])  # Objeto deque que contiene dos elementos(jugadores)

tablero = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']  # Lista con listas que contiene cadenas de caracteres
]


def rotar_turno():
    turno.rotate()  # Rotate = objeto de deque
    return turno[0]


def mostrar_tablero():  # Funcion que muestra tablero
    print('')
    for fila in tablero:  # Cada elemento es una lista
        print(fila)


def procesar_posicion(posicion):  # Verifica si la entrada es correcta
    fila, columna = posicion.split(",")  # Divide encontrando el caracter ,
    # Hay que restarle 1, ya que si el usuario escribe 1,1, se debería interpretar como 0,0
    # Se usa corchete para devolverlo como una lista
    return [int(fila)-1, int(columna)-1]


def posicion_correcta(posicion):
    # Verifica si poscion 0 y 1 estan en el rago de 0 y 2(es decir, de 1 a 3)
    if 0 <= posicion[0] <= 2 and 0 <= posicion[1] <= 2:
        if tablero[posicion[0]][posicion[1]] == " ":  # Verifica si esa posición está vacía
            return True
    return False


def juego():  # Función que llama a la función mostrar tablero
    mostrar_tablero()
    jugador = rotar_turno  # Resultado de la función rotar_turno
    while True:  # Ciclo while infinito, para salir SALIR
        posicion = input(
            f"Juega {jugador}. Elige posición: Fila o columna de 1 a 3")
        if posicion == 'salir':  # Si usa en la variable posicion 'salir' entonces break
            break
        jugador = rotar_turno()
        # Try: Captura cualquier error cuando se procese la posicion(ya que acepta cualquier número) que el usuario ingresó
        try:
            posicion_l = procesar_posicion(posicion)
        except:
            print(f'Error, posicion {posicion} no es válida')
            continue
        if posicion_correcta(posicion_l):
            print('Correcta')
        else:
            print('incorrecta')


juego()
