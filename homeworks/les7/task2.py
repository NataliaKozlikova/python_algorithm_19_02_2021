"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на
промежутке [0; 50). Выведите на экран исходный и отсортированный массивы. """

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 50
array = [round(random.uniform(MIN_ITEM, MAX_ITEM - 1), 2) for _ in range(SIZE)]
print('Исходный массив:')
print(array)


def merge_sort(data):
    if len(data) > 1:
        right_part = data[:len(data) // 2]
        left_part = data[len(data) // 2:]

        merge_sort(right_part)
        merge_sort(left_part)

        i, j, k = 0, 0, 0
        while i < len(right_part) and j < len(left_part):
            if left_part[j] > right_part[i]:
                data[k] = right_part[i]
                i += 1
            else:
                data[k] = left_part[j]
                j += 1
            k += 1

        while i < len(right_part):
            data[k] = right_part[i]
            i += 1
            k += 1

        while j < len(left_part):
            data[k] = left_part[j]
            j += 1
            k += 1

    #print(data)


merge_sort(array)
print('Отсортированный массив:')
print(array)
