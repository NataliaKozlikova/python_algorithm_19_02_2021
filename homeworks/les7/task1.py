"""
1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на 
промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы. """

import random

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM - 1) for _ in range(SIZE)]
print('Исходный массив:')
print(array)

print('Проходы:')


def bubble_sort(data):
    n = 1
    while n < len(data):
        spam = 0
        for i in range(len(data) - 1):
            if data[i] < data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
                spam += 1
        if spam == 0:
            break
        n += 1
        print(f'Проход {n - 1} {data}')


bubble_sort(array)

print('Отсортированный массив:')
print(array)
