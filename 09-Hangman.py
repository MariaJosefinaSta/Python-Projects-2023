""" import random
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

    lives = 6

    # Mientras la longitud de las palabras sea mayor que 0 continuar iterando
    while len(word_letters) > 0 and lives > 0:
        # Convierte la lista en una cadena separada por comas o espacio
        print('You have', lives, 'used these letters: ', ' '.join(used_letters))

        # Crea lista donde se muestra cada letra que adivinó y las letras que no adivinó como guiones
        word_list = [
            letter if letter in used_letters else '-' for letter in word]
        # toma la lista anterior y la une con un espacio para crear una cadena usando esa lista
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        # Si este es un carácter válido en el alfabeto y aún no lo he usado
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)  # Agregarlo a este conjunto
            if user_letter in word_letters:  # Si la letra que acabo de adivinar está en la palabra, borrar las palabras que no la tengan
                word_letters.remove(user_letter)
                print('')

            else:
                lives = lives - 1
                print('Letter is not in word')

        elif user_letter in used_letters:
            print('You have already used that character')

        else:
            print('Invalid character')


user_input = input('Type something: ')
print(user_input)
 """

import random
from words import words
from hangman_visual import lives_visual_dict
import string


def get_valid_word(words):
    word = random.choice(words)  # randomly chooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed

    lives = 7

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print('You have', lives, 'lives left and you have used these letters: ',
              ' '.join(used_letters))

        # what current word is (ie W - R D)
        word_list = [
            letter if letter in used_letters else '-' for letter in word]
        print(lives_visual_dict[lives])
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                lives = lives - 1  # takes away a life if wrong
                print('\nYour letter,', user_letter, 'is not in the word.')

        elif user_letter in used_letters:
            print('\nYou have already used that letter. Guess another letter.')

        else:
            print('\nThat is not a valid letter.')

    # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print(lives_visual_dict[lives])
        print('You died, sorry. The word was', word)
    else:
        print('YAY! You guessed the word', word, '!!')


if __name__ == '__main__':
    hangman()
