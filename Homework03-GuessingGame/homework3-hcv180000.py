# Homework 3
# Hannah Valena - HCV180000
# CS 4395.001: Human Language Technologies

import sys
import nltk
import re
from collections import Counter
from datetime import datetime
from nltk import WordNetLemmatizer
from nltk.corpus import stopwords
from random import seed
from random import randint


def preprocess_text(text_raw):
    """
    :param text_raw: raw text from the input file
    :return: a tuple containing a list of preprocessed tokens and a list of nouns
    """

    print(f'\nPreprocessing text...')

    tokens_text = nltk.word_tokenize(text_raw)

    # lowercase
    tokens_lower = [t.lower() for t in tokens_text]

    # remove non-alpha and stopwords and length <= 5
    tokens_pp = [t for t in tokens_lower if t.isalpha() and
                 t not in stopwords.words('english') and
                 len(t) > 5]

    # lemmatize and get unique lemmas
    wnl = WordNetLemmatizer()
    lemmas = [wnl.lemmatize(t) for t in tokens_pp]
    lemmas_unique = list(set(lemmas))

    # pos tagging
    tags = nltk.pos_tag(lemmas_unique)
    print(f'\tFirst 20 tagged items: ')
    i = 1
    for t in tags[:20]:
        print(f'\t\t{i}. {t}')
        i += 1

    # list of only nouns
    nouns = [n[0] for n in tags if n[1][0] == 'N']

    # number of tokens and nouns
    print(f'\n\tNumber of tokens: {len(tokens_pp)}')
    print(f'\tNumber of nouns: {len(nouns)}')

    # return tokens and nouns
    print('Preprocessing completed.')
    return tokens_pp, nouns


def play_guessing_game(words):
    """
    :param words: 50 most common nouns in the input file, one is chosen randomly for each game
    :return: n/a
    """
    print('\nLet\'s play a guessing game!')
    print('-' * 100)
    print('Rules: ')
    print('\t1. You start with 5 points.')
    print('\t2. If you guess a letter correctly, you get 1 point!')
    print('\t3. If you guess a letter incorrectly, you lose 1 point.')
    print('\t4. The game ends if your score is negative OR if you guess \'!\' as a letter.')
    print('-' * 100)
    print('Let\'s start!')

    # pick a random word
    seed(datetime.now().timestamp())
    idx = randint(0, 50)
    word = words[idx]

    points = 5
    word_guess = '_ ' * len(word)
    guessed_letters = []

    # start guessing
    while points >= 0:
        print(f'\nYour score is: {points}')
        print('Your word is: ' + word_guess)
        print('Letters already guessed: ' + ' '.join(guessed_letters))
        letter_guess = input('Guess a letter: ').lower()

        # end guessing game
        if letter_guess == '!':
            print(f'\nEnding the guessing game. Your final score is {points}. The word was {word}.')
            break

        # invalid input
        while len(letter_guess) != 1 or not letter_guess.isalpha() or letter_guess in guessed_letters:
            letter_guess = input('You must guess 1 letter at a time. You cannot repeat guesses. '
                                 'Please enter another guess: ')

        guessed_letters.append(letter_guess)

        # correct guess
        if word.count(letter_guess) > 0:
            points += 1
            print(f'Correct!')

            # update word_guess
            indices = [_.start() for _ in re.finditer(letter_guess, word)]
            word_temp = list(word_guess)
            for x in indices:
                word_temp[x * 2] = letter_guess
            word_guess = ''.join(word_temp)

            # check if word is fully guessed
            if word_guess.replace(' ', '') == word:
                print(f'\nYou solved it! Your final score is {points}. The word was {word}.')
                break;
        # incorrect guess
        else:
            points -= 1

            # end guessing game
            if points < 0:
                print(f'\nYou failed. Your final score is {points}. The word was {word}.')
                break

            print(f'Wrong. Sorry, try again.')

    # play another game
    play_again = input('Would you like to play again? Y/N: ')
    if "y" in play_again.lower():
        play_guessing_game(words)
    else:
        print('Thanks for playing!')


if __name__ == '__main__':
    # check sysarg for filename
    if len(sys.argv) < 2:
        print('Error: You must specify a sysarg for the filename')
        quit()

    # read input file as raw text
    file_name = sys.argv[1]
    file = open(file_name, 'r')
    raw_text = file.read()
    file.close()

    # tokenize raw text
    tokens = nltk.word_tokenize(raw_text)
    tokens_set = set(tokens)

    # calculate lexical diversity of tokenized text
    print("\nLexical diversity: %.2f" % (len(tokens_set) / len(tokens)))

    # preprocess raw text
    tokens_nouns = preprocess_text(raw_text)

    # dict{noun : count of noun in tokens}
    tokens_nouns = [n for n in tokens_nouns[0] if n in tokens_nouns[1]]
    noun_dict = dict(Counter(tokens_nouns))

    # print and save 50 most common nouns
    print(f'\n50 most common nouns and their occurrences: ')
    num = 1
    nouns_common = sorted(noun_dict, key=noun_dict.get, reverse=True)[:50]
    for noun in nouns_common:
        print(f'\t{num}. {noun}, {noun_dict.get(noun)}')
        num += 1

    # guessing game
    play_guessing_game(nouns_common)

