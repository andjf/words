from words import get_words_set
from string import ascii_lowercase
from sys import argv

assert len(argv) == 2
word = argv[-1].lower()
assert all(letter in ascii_lowercase for letter in word)

english_words_set = get_words_set()

order = [
    "qwertyuiop",
    "asdfghjkl",
    "zxcvbnm",
]

next_letter = {letter: row[i + 1] for row in order for i, letter in enumerate(row) if i + 1 < len(row)}
prev_letter = {letter: row[i - 1] for row in order for i, letter in enumerate(row) if i - 1 >= 0}

def replace_letter_at_index(word, index, replacement_char):
    return word[:index] + replacement_char + word[index + 1:]

def get_possible(word, letter_set):
    for i, letter in enumerate(word.lower()):
        if letter in letter_set:
            new_word = replace_letter_at_index(word, i, letter_set[letter])
            if new_word in english_words_set:
                yield new_word

def get_prev_possible(word):
    return get_possible(word, prev_letter)

def get_next_possible(word):
    return get_possible(word, next_letter)

print("If the given word was first, second words could include:", " ".join(get_next_possible(word)))
print("If the given word was second, first words could include:", " ".join(get_prev_possible(word)))
