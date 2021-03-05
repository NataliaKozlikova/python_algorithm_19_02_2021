"""
3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""

import random

SIZE = 20
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'Исходный массив:   {array}')

min_el = 0
max_el = 0
for i in range(len(array)):
    if array[i] < array[min_el]:
        min_el = i
    elif array[i] > array[max_el]:
        max_el = i
print(f'Мин.эл.массива: {array[min_el]} на {min_el+1} месте\nМакс.эл.массива: {array[max_el]} на {max_el+1} месте')
array[min_el], array[max_el] = array[max_el], array[min_el]

print(f'Измененный массив: {array}')
