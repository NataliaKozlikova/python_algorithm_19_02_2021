"""
2. Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560,
в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

Подсчитать, сколько было выделено памяти под переменные. Проанализировать результат и определить вариант
с наиболее эффективным использованием памяти.
"""

import sys


def show(obj):
    print(f'{type(obj)=}, {sys.getsizeof(obj)=}, {obj=}')
    sum_mem = 0
    count = 0
    type_obj = []
    if hasattr(obj, '__iter__'):
        if hasattr(obj, 'items'):
            for key, value in obj.items():
                show(key)
                show(value)
                sum_mem += sys.getsizeof(key) + sys.getsizeof(value)
                count += 1
                type_obj.append(type(key))
                type_obj.append(type(value))
        elif not isinstance(obj, str):
            for item in obj:
                show(item)
                sum_mem += sys.getsizeof(item)
                count += 1
                type_obj.append(type(item))
    return f'Под {count} переменные ({type_obj}) выделено {sum_mem} байта памяти'


# Windows 10, 64-разрядная. Python 3.9.2

# Вариант 1
# Под 3 переменные ([<class 'int'>, <class 'int'>, <class 'int'>]) выделено 80 байт памяти

num = int(input('Введите натуральное число: '))
even = odd = 0
while num > 0:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
    num = num // 10

print(f'{even} четные цифры, {odd} нечетные цифры')

print(show([num, even, odd]))

# Вариант 2
# Под 4 переменные ([<class 'str'>, <class 'int'>, <class 'int'>, <class 'str'>]) выделено 161 байт памяти

num2 = input('Введите целое число: ')
even2 = odd2 = 0
for i in num2:
    if i in {'0', '2', '4', '6', '8'}:
        even2 += 1
    else:
        odd2 += 1
print(f"четных - {even2}, нечетных - {odd2}")

print(show([num2, even2, odd2, i]))

# Вариант 3
# Под 4 переменные ([<class 'str'>, <class 'list'>, <class 'list'>, <class 'str'>]) выделено 281 байт памяти

num3 = input('Введите целое число: ')
even3 = []
odd3 = []
for i in num3:
    if int(i) % 2 == 0:
        even3.append(i)
    else:
        odd3.append(i)
print(f'{len(even3)} - четных, {len(odd3)} - нечетных')

print(show([num3, even3, odd3, i]))

"""
ВЫВОД
Вариант №1 считаю оптимальным, т.к. под переменные задействовано 80 байт памяти, 
что в 2 раза меньше, чем в Варианте №2 (161 байт) и в 3,5 раза меньше, чем в Варианте №3 (281 байт). 
Экономия памяти в Варианте №1 - за счет использования исключительно переменных типа INT, 
тогда как в остальных вариантах также задействованы типы STR и LIST, которые требуеют больше памяти чем INT.
"""