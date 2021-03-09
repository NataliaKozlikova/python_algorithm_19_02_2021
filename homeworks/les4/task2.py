"""
Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать на
ход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.
Первый — с помощью алгоритма «Решето Эратосфена».
Второй — без использования «Решета Эратосфена».
"""

import timeit
import cProfile


# Вариант 1
def eratos_sieve(n):
    count = 1
    start = 3
    end = 4 * n

    sieve = [i for i in range(start, end) if i % 2 != 0]
    prime = [2]

    if n == 1:
        return 2
    while count < n:
        for i in range(len(sieve)):
            if sieve[i] != 0:
                count += 1
                if count == n:
                    return sieve[i]
                j = i + sieve[i]
                while j < len(sieve):
                    sieve[j] = 0
                    j += sieve[i]
        prime.extend([i for i in sieve if i != 0])
        start, end = end, end + 2 * n
        sieve = [i for i in range(start, end) if i % 2 != 0]
        for i in range(len(sieve)):
            for num in prime:
                if sieve[i] % num == 0:
                    sieve[i] = 0
                    break


print(timeit.timeit('eratos_sieve(10)', number=100, globals=globals()))  # 0.00043450000000000086
print(timeit.timeit('eratos_sieve(100)', number=100, globals=globals()))  # 0.016252900000000004
print(timeit.timeit('eratos_sieve(1_000)', number=100, globals=globals()))  # 1.4662002
print(timeit.timeit('eratos_sieve(2_000)', number=100, globals=globals()))  # 8.141481899999999

cProfile.run('eratos_sieve(10)')
cProfile.run('eratos_sieve(100)')
cProfile.run('eratos_sieve(1_000)')
cProfile.run('eratos_sieve(2_000)')

""" 27 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 task2.py:13(eratos_sieve)
        1    0.000    0.000    0.000    0.000 task2.py:18(<listcomp>)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
       22    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


         353 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 task2.py:13(eratos_sieve)
        1    0.000    0.000    0.000    0.000 task2.py:18(<listcomp>)
        1    0.000    0.000    0.000    0.000 task2.py:33(<listcomp>)
        1    0.000    0.000    0.000    0.000 task2.py:35(<listcomp>)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
      345    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method 'extend' of 'list' objects}


         4289 function calls in 0.016 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.016    0.016 <string>:1(<module>)
        1    0.015    0.015    0.016    0.016 task2.py:13(eratos_sieve)
        1    0.000    0.000    0.000    0.000 task2.py:18(<listcomp>)
        2    0.000    0.000    0.000    0.000 task2.py:33(<listcomp>)
        2    0.000    0.000    0.000    0.000 task2.py:35(<listcomp>)
        1    0.000    0.000    0.016    0.016 {built-in method builtins.exec}
     4278    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        2    0.000    0.000    0.000    0.000 {method 'extend' of 'list' objects}


         8969 function calls in 0.083 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.083    0.083 <string>:1(<module>)
        1    0.081    0.081    0.083    0.083 task2.py:13(eratos_sieve)
        1    0.000    0.000    0.000    0.000 task2.py:18(<listcomp>)
        3    0.000    0.000    0.000    0.000 task2.py:33(<listcomp>)
        3    0.000    0.000    0.000    0.000 task2.py:35(<listcomp>)
        1    0.000    0.000    0.083    0.083 {built-in method builtins.exec}
     8955    0.001    0.000    0.001    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        3    0.000    0.000    0.000    0.000 {method 'extend' of 'list' objects}
"""


# Вариант 2
def prime_by_number(n):
    count = 1
    number = 1
    prime = [2]
    if n == 1:
        return 2
    while count != n:
        number += 2
        for num in prime:
            if number % num == 0:
                break
        else:
            count += 1
            prime.append(number)
    return number


print(timeit.timeit('prime_by_number(10)', number=100, globals=globals()))  # 0.000268500000000671
print(timeit.timeit('prime_by_number(100)', number=100, globals=globals()))  # 0.01520559999999982
print(timeit.timeit('prime_by_number(1_000)', number=100, globals=globals()))  # 1.8173857000000009
print(timeit.timeit('prime_by_number(2_000)', number=100, globals=globals()))  # 7.519395600000001

cProfile.run('prime_by_number(10)')
cProfile.run('prime_by_number(100)')
cProfile.run('prime_by_number(1_000)')
cProfile.run('prime_by_number(2_000)')

"""
13 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 task2.py:53(prime_by_number)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        9    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


         103 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 task2.py:53(prime_by_number)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
       99    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


         1003 function calls in 0.018 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.018    0.018 <string>:1(<module>)
        1    0.018    0.018    0.018    0.018 task2.py:53(prime_by_number)
        1    0.000    0.000    0.018    0.018 {built-in method builtins.exec}
      999    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


         2003 function calls in 0.076 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.076    0.076 <string>:1(<module>)
        1    0.076    0.076    0.076    0.076 task2.py:53(prime_by_number)
        1    0.000    0.000    0.076    0.076 {built-in method builtins.exec}
     1999    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

# Вывод:
# На основе данных полученных с помощью функции timeint оба алгоритма имееют квадратичную сложность O(n2),
# т.к. при увеличении объема данных время растет ~ по функции у = x ** 2.
# Вариант №2 работает немного быстре:
# Вар.1                      Вар.2
# # 0.00043450000000000086  # 0.000268500000000671
# 0.016252900000000004      # 0.01520559999999982
# 1.4662002                 # 1.8173857000000009
# 8.141481899999999         # 7.519395600000001
