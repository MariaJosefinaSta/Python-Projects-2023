class TicTacToe:
    def __init__(self):
        # Tablero hecho de lista, asignando índice con len 9, que representa tablero de 3x3
        self.board = [' ' for _ in range(9)]
        self.current_winner = None  # Variable que hace un seguimiento de si hay un ganador

    def print_board(self):  # Imprimir tablero
        # i en rango de 3 a la derecha, i multiplicado por 3, i  más 1: 3 veces
        for row in [self.board[i*3:(i+1)*3]for i in range(3)]:
            print(" |  " + " |  ".join(row) + " |  ")

    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j*3, (j+1)*3)]
                        for j in range(3)]
        # indice que solo devuelva qué indices están en las fials para cada una de las filas, 0, 1, 2
        # 3, 4, 5
        # 6, 7, 8
        for row in number_board:
            print(" |  " + " |  ".join(row) + " |  ")

    def aviable_mover(self):
        # Si el spot está vacío que ponga i en ese spot
        return [i for i, spot in enumerate(self.board) if spot == " "]
        # # moves = []
        # for (i, spot) in enumerate(self.board):
        #     if spot == " ":
        #         moves.append(i)
        # return moves
