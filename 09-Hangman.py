import random
from words import words

import string
string.ascii_uppercase
'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:  # Mientras el guión o espacio estén en la palabra siga eligiendo la palabra
        word = random.choice(words)

    return word.upper()


def hangman():
    # Seguimientode letras y palabras que adivinamos y
    word = get_valid_word(words)
    # Seguimiento de lo que es una letra válida, variable word_letters guarda letras válidas de una palabra, set representa conjuntos
    word_letters = set(word)
    # Lista predeterminada de caracteres
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # Pista al usuario de lo que ha adivinado

    while len(word_letters) > 0:

        user_letter = input('Guess a letter: ').upper()
        # Si este es un carácter válido en el alfabeto y aún no lo he usado
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)  # Agregarlo a este conjunto
            if user_letter in word_letters:  # Si la letra que acabo de adivinar está en la palabra, borrar las palabras que no la tengan
                word_letters.remove(user_letter)

        elif user_letter in used_letters:
            print('You have already used that character')

        else:
            print('Invalid character')


user_input = input('Type something: ')
print(user_input)
