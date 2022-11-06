'''Напишите функцию longest_word_in_file, которая принимает имя файла и внутри его содержимого находит самое длинное слово и возвращает его в качестве ответа. В случае,  если есть несколько слов с максимальной длиной, нужно вернуть слово, которое встречается последнее в тексте.

При этом слова в тексте отделяются друг от друга пробелами, любые другие знаки пунктуации необходимо исключить.  И также учитывайте, что слова в тестах будут как на русском языке, так и на английском

Все возможные знаки пунктуации можно получить из модуля string

from string import punctuation'''

def longest_word_in_file(file_name):
    file = open(file_name, 'r', encoding='utf-8')
    max_word = ''
    for line in file:
        words = line.split()
        for word in words:
            word_without_punct = remove_punct(word)
            if len(max_word) <= len(word_without_punct):
                max_word = word_without_punct
    file.close()
    return max_word

def remove_punct(word):
    from string import punctuation
    for punct in punctuation:
        if punct in word:        
            word = word.replace(punct, '')
    return word
