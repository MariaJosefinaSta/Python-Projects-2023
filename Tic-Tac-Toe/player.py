import random
import math


class Player:
    def __init__(self, letter):  # Inicializar class con la letra que va a representar al jugador x or o

        self.letter = letter

    # Para que cada jugador obtenga su próximo movimiento
    def get_move(self, game):
        pass


class RandomComputerPlayer(Player):

    def __init__(self, letter):
        # La función super() de Python devuelve objetos representados en la clase principal y es muy útil en herencias múltiples y multinivel para encontrar qué clase está extendiendo primero la clase secundaria.
        super().__init__(letter)

    def get_move(self, game):
        pass

        # Elige un spot random para el próximo movimiento
        square = random.choice(game.aviable_moves())
        return square


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None  # Por que el ususuario no ingresó nada, cuando ingrese retorna True
        while not valid_square:
            square = input(self.letter + " \"s turn. Input move(0-9): ")

            try:
                val = int(square)
                if val not in game.aviable_moves():
                    # Si el usuario ingresa un valor de otro tipo que no sea entero devuelve errar
                    raise ValueError
