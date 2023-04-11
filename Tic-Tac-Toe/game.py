class TicTacToe:
    def __init__(self):
        # Tablero hecho de lista, asignando índice con len 9, que representa tablero de 3x3
        self.board = [' ' for _ in range(9)]
        self.current_winner = None  # Variable que hace un seguimiento de si hay un ganador

    def print_board(self):  # Imprimir tablero
        for row in [self.board[i*3:(i+1)*3]for i in range(3)]:
