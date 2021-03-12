"""Написать программу сложения и умножения двух положительных целых шестнадцатеричных чисел. При этом каждое число
представляется как коллекция, элементы которой — цифры числа. Например, пользователь ввёл A2 и C4F. Нужно сохранить
их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
* произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’] """

from collections import deque

a = list(input('Введите 1-е шестнадцатиричное число: ').upper())
b = list(input('Введите 2-е шестнадцатиричное число: ').upper())

HEX_NUM = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
           'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
           0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
           10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
result = deque()
transfer = 0

if len(b) > len(a):
    a, b = deque(b), deque(a)
else:
    a, b = deque(a), deque(b)

while a:
    if b:
        temp = HEX_NUM[a.pop()] + HEX_NUM[b.pop()] + transfer
    else:
        temp = HEX_NUM[a.pop()] + transfer
    transfer = 0
    if temp < 16:
        result.appendleft(HEX_NUM[temp])
    else:
        result.appendleft(HEX_NUM[temp - 16])
        transfer = 1

if transfer:
    result.appendleft('1')

print(f'Сумма = {result}')
