"""
1. Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
Требуется вернуть количество различных подстрок в этой строке. Примечание: в сумму не включаем пустую строку и строку
целиком.
"""

import hashlib


def sum_sub(string):
    sum_s = set()
    for i in range(len(string)):
        for j in range(len(string), i, -1):
            hash_string = hashlib.sha1(string[i:j].encode('utf-8')).hexdigest()
            sum_s.add(hash_string)
    return f'{len(sum_s) - 1} различных подстрок в строке "{string}"'


print(sum_sub(input('Введите строку: ')))
