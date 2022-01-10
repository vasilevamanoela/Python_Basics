import math
import sys

word = input()
list_of_letters = ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y']
max_sum = -sys.maxsize
best_word = ''

while word != 'End of words':
    sum_word_letters = 0
    for letter in word:
        sum_word_letters += ord(letter)

    if word[0] in list_of_letters:
        sum_word_letters *= len(word)
    else:
        sum_word_letters = math.floor(sum_word_letters / len(word))

    if sum_word_letters > max_sum:
        max_sum = sum_word_letters
        best_word = word

    word = input()

print(f"The most powerful word is {best_word} - {max_sum}" )