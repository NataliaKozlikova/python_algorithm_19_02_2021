"""
В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
Это два абсолютно разных значения.
"""

import random

SIZE = 100
MIN_ITEM = -50
MAX_ITEM = 50
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

minus = []
max_neg = 0
for i in array:
    if i < 0:
        minus.append(i)

for i in range(len(minus)):
    if minus[i] > minus[max_neg]:
        max_neg = i

print(f'Максимальный отрицательный элемент массива: {minus[max_neg]} на позиции {array.index(minus[max_neg])}')
