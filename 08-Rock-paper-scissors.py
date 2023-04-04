import random


def play():

    user = input(
        "Whats your choise? 'r' for rock, 'p' for paper, 's' for scissors")
    # la computadora elige una opción random
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'Tie'  # Si tienen la misma elección es un empate

    if is_win(user, computer):
        return 'You won!'  # r > s, s > p, p > r
        # Piedra le gana a tijera, tijera le gana a papel, papel le gana a piedra
    return 'You lost!'  # Si no se ejecuta tie ni won
    # opponent = computer user = playe r


def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
            or (player == 'p' and opponent == 'r'):
        return True


print(play())
