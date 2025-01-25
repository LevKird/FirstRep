from random import choice
from secret_words import words

man = [
    """
 |--------|
 |        o
 |       /|\\
 |       / \\
 |
_|_
""",
  """
 |--------|
 |        o
 |       /|\\
 |       / 
 |
_|_
""",
"""
 |--------|
 |        o
 |       /|\\
 |      
 |
_|_
""",
  """
 |--------|
 |        o
 |       /|
 |       
 |
_|_
""",
"""
 |--------|
 |        o
 |        |
 |       
 |
_|_
""",
  """
 |--------|
 |        o
 |       
 |       
 |
_|_
""",
 """
 |--------|
 |        
 |       
 |       
 |
_|_
""",

]


def get_word(words):
    return choice(words).upper()


def is_alpha20(word_completion):
    if word_completion.count('_') == 0:
        return True
    return False


def inp_char():
    ch_ = input('Введите букву. ')
    if ch_.isalpha():
        return ch_.upper()
    else:
        print('Неправильный ввод')
        return inp_char()


def count_char(word, char):
    caunt = 0
    indexes = []
    for i in word:
        if i == char:
            indexes.append(caunt)
        caunt += 1
    return indexes


def make_word_completion(word_completion, char, indexes):
    if len(indexes) == 0:
        return word_completion
    else:
        word_completion = word_completion.split(' ')
        for i in indexes:
            word_completion[i] = char
    word_completion = ' '.join(word_completion)
    return word_completion


def play(word):
    word_completion = '_ ' * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("\033[1;32;40mМы загадали слово, Вы должны его угадать.\033[0;0m")
    #print('\U0001F497')
    #print('\U0001F5A4')
    while tries >= 0:
        if is_alpha20(word_completion):
            print(f'\033[1;32;40mПоздравляем вы угадали слово - {word}\033[0;1m')
            guessed_words.append(word)
            break
        if tries == 0:
            print('Вы проиграли.')
            print(man[tries])
            break
        print(word_completion)
        print(man[tries])
        true_ch = inp_char()
        indexes = count_char(word, true_ch)
        if true_ch not in guessed_letters:
            guessed_letters.append(true_ch)
        else:
            print('Такая буква уже была.')
            continue

        if true_ch in word:
            word_completion = make_word_completion(word_completion, true_ch, indexes)
            continue
        else:
            tries -= 1
            continue


while True:
    play(get_word(words))
    ans = input('Хотите повторить? Да-Нет ')
    if ans.lower() == 'нет':
        break
    else:
        continue
        
