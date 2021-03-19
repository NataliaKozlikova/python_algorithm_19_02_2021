"""
3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше
медианы, в другой — не больше медианы. """

import random

M = 5
SIZE = 2 * M + 1
MIN_ITEM = 0
MAX_ITEM = 50
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print('Исходный массив:')
print(array)


def find_median(data):
    i = 1
    while i < len(data):
        if data[i - 1] <= data[i]:
            i += 1
        else:
            data[i-1], data[i] = data[i], data[i-1]
            i -= 1
            if i == 0:
                i = 1
    return f'Отсортированный массив\n{data}\nМедиана: {data[len(data) // 2]}'


print(find_median(array))
