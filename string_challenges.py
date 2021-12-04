# Вывести последнюю букву в слове
from typing import Counter

word = 'Архангельск'
print('Последняя буква в слове: ', word[-1])
# ???


# Вывести количество букв "а" в слове
word = 'Архангельск'
print('Количество букв "а" в слове: ', word.lower().count('а')) 
# ???


# Вывести количество гласных букв в слове
word = 'Архангельск'
word_low = word.lower()
vowels_tuple = ('а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е')
vowels_number = 0
 
for letter in word_low:
    if letter in vowels_tuple:
        vowels_number +=1
print(f'Количество гласных букв в слове: {vowels_number}')
# ???


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
words = sentence.split()
number_of_words = len(words)
print(f'Количество слов в предложении: {number_of_words}')
# ???


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
words = sentence.split()
for word in words:
    print(word[0])
# ???


# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
words = sentence.split()
total_length = 0
for word in words:
    total_length = total_length + len(word)
number_of_words = len(words)
average_word_length = total_length/number_of_words
print(f'Усреднённая длина слова в предложении: {average_word_length}')
# ???