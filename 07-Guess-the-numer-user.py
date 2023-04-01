import random


def computer_guess(x):

    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # Para que el programa al adivinar de una no termine tan rápido
        feedback = input(f'Is {guess} to high (H), too low(L), or correct (C)')
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess+1

        print(f'Congrats, the computer guess your numer {guess}')


computer_guess(10)
