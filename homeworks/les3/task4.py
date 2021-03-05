"""
Определить, какое число в массиве встречается чаще всего.
"""

import random

SIZE = 100
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

num = array[0]
max_count = 1
for i in range(len(array) - 1):
    count = 1
    for j in range(i + 1, len(array)):
        if array[i] == array[j]:
            count += 1
    if count > max_count:
        max_count = count
        num = array[i]

if max_count > 1:
    print(f'Число {num} встречатся {max_count} раз(а)')
else:
    print('Все элементы уникальны')
