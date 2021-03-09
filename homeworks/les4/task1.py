"""
В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
Это два абсолютно разных значения.
"""

import random
import timeit
import cProfile

# # Вариант 1
def max_neg(size, min_item, max_item):
    array = [random.randint(min_item, max_item) for _ in range(size)]
    minus = []
    index = 0
    for i in array:
        if i < 0:
            minus.append(i)
    for i in range(len(minus)):
        if minus[i] > minus[index]:
            index = i
    return minus[index], array.index(minus[index])


print(timeit.timeit('max_neg(100, -750, 750)', number=100, globals=globals()))        # 0.0133051
print(timeit.timeit('max_neg(1_000, -750, 750)', number=100, globals=globals()))      # 0.1393315
print(timeit.timeit('max_neg(10_000, -750, 750)', number=100, globals=globals()))     # 1.4489410999999999
print(timeit.timeit('max_neg(100_000, -750, 750)', number=100, globals=globals()))    # 12.216288800000001

cProfile.run('max_neg(100, -750, 750)')
cProfile.run('max_neg(1_000, -750, 750)')
cProfile.run('max_neg(10_000, -750, 750)')
cProfile.run('max_neg(100_000, -750, 750)')

# Алгоритм в Варианте №1 имеет O(n) линейную сложность

""" 606 function calls in 0.002 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
      100    0.001    0.000    0.001    0.000 random.py:237(_randbelow_with_getrandbits)
      100    0.000    0.000    0.001    0.000 random.py:290(randrange)
      100    0.000    0.000    0.001    0.000 random.py:334(randint)
        1    0.000    0.000    0.001    0.001 task1.py:13(max_neg)
        1    0.000    0.000    0.001    0.001 task1.py:14(<listcomp>)
        1    0.001    0.001    0.002    0.002 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
       50    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
      100    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
      149    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
        1    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}


         5876 function calls in 0.003 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.003    0.003 <string>:1(<module>)
     1000    0.001    0.000    0.001    0.000 random.py:237(_randbelow_with_getrandbits)
     1000    0.001    0.000    0.002    0.000 random.py:290(randrange)
     1000    0.000    0.000    0.002    0.000 random.py:334(randint)
        1    0.000    0.000    0.003    0.003 task1.py:13(max_neg)
        1    0.000    0.000    0.003    0.003 task1.py:14(<listcomp>)
        1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
      508    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
     1000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
     1361    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
        1    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}


         58782 function calls in 0.029 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.029    0.029 <string>:1(<module>)
    10000    0.007    0.000    0.010    0.000 random.py:237(_randbelow_with_getrandbits)
    10000    0.008    0.000    0.018    0.000 random.py:290(randrange)
    10000    0.004    0.000    0.022    0.000 random.py:334(randint)
        1    0.002    0.002    0.029    0.029 task1.py:13(max_neg)
        1    0.004    0.004    0.027    0.027 task1.py:14(<listcomp>)
        1    0.000    0.000    0.029    0.029 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
     5005    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
    10000    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    13770    0.002    0.000    0.002    0.000 {method 'getrandbits' of '_random.Random' objects}
        1    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}


         586742 function calls in 0.353 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.005    0.005    0.353    0.353 <string>:1(<module>)
   100000    0.079    0.000    0.118    0.000 random.py:237(_randbelow_with_getrandbits)
   100000    0.108    0.000    0.226    0.000 random.py:290(randrange)
   100000    0.050    0.000    0.276    0.000 random.py:334(randint)
        1    0.018    0.018    0.348    0.348 task1.py:13(max_neg)
        1    0.050    0.050    0.326    0.326 task1.py:14(<listcomp>)
        1    0.000    0.000    0.353    0.353 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
    50168    0.005    0.000    0.005    0.000 {method 'append' of 'list' objects}
   100000    0.012    0.000    0.012    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
   136567    0.027    0.000    0.027    0.000 {method 'getrandbits' of '_random.Random' objects}
        1    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}

"""

# Вариант 2
def max_minus(size, min_item, max_item):
    array = [random.randint(min_item, max_item) for _ in range(size)]
    minus = []
    for i in array:
        if i < 0:
            minus.append(i)
    neg = max(minus)
    return neg, array.index(neg)


print(timeit.timeit('max_minus(100, -750, 750)', number=100, globals=globals()))        # 0.0137269
print(timeit.timeit('max_minus(1_000, -750, 750)', number=100, globals=globals()))      # 0.12708389999999997
print(timeit.timeit('max_minus(10_000, -750, 750)', number=100, globals=globals()))     # 1.3615561
print(timeit.timeit('max_minus(100_000, -750, 750)', number=100, globals=globals()))    # 11.7607468

cProfile.run('max_minus(100, -750, 750)')
cProfile.run('max_minus(1_000, -750, 750)')
cProfile.run('max_minus(10_000, -750, 750)')
cProfile.run('max_minus(100_000, -750, 750)')

# Алгоритм в Варианте №2 имеет O(n) линейную сложность

""" 
   584 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
      100    0.000    0.000    0.000    0.000 random.py:237(_randbelow_with_getrandbits)
      100    0.000    0.000    0.000    0.000 random.py:290(randrange)
      100    0.000    0.000    0.000    0.000 random.py:334(randint)
        1    0.000    0.000    0.000    0.000 task1.py:118(max_minus)
        1    0.000    0.000    0.000    0.000 task1.py:119(<listcomp>)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.max}
       52    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
      100    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
      125    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
        1    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}


         5868 function calls in 0.003 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.003    0.003 <string>:1(<module>)
     1000    0.001    0.000    0.001    0.000 random.py:237(_randbelow_with_getrandbits)
     1000    0.001    0.000    0.002    0.000 random.py:290(randrange)
     1000    0.000    0.000    0.002    0.000 random.py:334(randint)
        1    0.000    0.000    0.003    0.003 task1.py:118(max_minus)
        1    0.000    0.000    0.003    0.003 task1.py:119(<listcomp>)
        1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.max}
      490    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
     1000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
     1371    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
        1    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}


         58547 function calls in 0.028 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.028    0.028 <string>:1(<module>)
    10000    0.007    0.000    0.009    0.000 random.py:237(_randbelow_with_getrandbits)
    10000    0.008    0.000    0.018    0.000 random.py:290(randrange)
    10000    0.004    0.000    0.022    0.000 random.py:334(randint)
        1    0.001    0.001    0.028    0.028 task1.py:118(max_minus)
        1    0.004    0.004    0.026    0.026 task1.py:119(<listcomp>)
        1    0.000    0.000    0.028    0.028 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.max}
     4934    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
    10000    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    13606    0.002    0.000    0.002    0.000 {method 'getrandbits' of '_random.Random' objects}
        1    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}


         586150 function calls in 0.298 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.003    0.003    0.298    0.298 <string>:1(<module>)
   100000    0.070    0.000    0.101    0.000 random.py:237(_randbelow_with_getrandbits)
   100000    0.087    0.000    0.188    0.000 random.py:290(randrange)
   100000    0.046    0.000    0.234    0.000 random.py:334(randint)
        1    0.012    0.012    0.295    0.295 task1.py:118(max_minus)
        1    0.043    0.043    0.277    0.277 task1.py:119(<listcomp>)
        1    0.000    0.000    0.298    0.298 {built-in method builtins.exec}
        1    0.001    0.001    0.001    0.001 {built-in method builtins.max}
    49795    0.005    0.000    0.005    0.000 {method 'append' of 'list' objects}
   100000    0.011    0.000    0.011    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
   136348    0.020    0.000    0.020    0.000 {method 'getrandbits' of '_random.Random' objects}
        1    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}
"""

# Вариант 3
def max_below_zero(size, min_item, max_item):
    array = [random.randint(min_item, max_item) for _ in range(size)]
    i = 0
    index = -1
    while i < len(array):
        if array[i] < 0 and index == -1:
            index = i
        elif 0 > array[i] > array[index]:
            index = i
        i += 1
    return array[index], index

print(timeit.timeit('max_below_zero(100, -750, 750)', number=100, globals=globals()))        # 0.013298400000000002
print(timeit.timeit('max_below_zero(1_000, -750, 750)', number=100, globals=globals()))      # 0.14892480000000002
print(timeit.timeit('max_below_zero(10_000, -750, 750)', number=100, globals=globals()))     # 1.6045604
print(timeit.timeit('max_below_zero(100_000, -750, 750)', number=100, globals=globals()))    # 13.3031404

cProfile.run('max_below_zero(100, -750, 750)')
cProfile.run('max_below_zero(1_000, -750, 750)')
cProfile.run('max_below_zero(10_000, -750, 750)')
cProfile.run('max_below_zero(100_000, -750, 750)')

# Алгоритм в Варианте №3 имеет O(n) линейную сложность

"""
   648 function calls in 0.001 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
      100    0.000    0.000    0.000    0.000 random.py:237(_randbelow_with_getrandbits)
      100    0.000    0.000    0.000    0.000 random.py:290(randrange)
      100    0.000    0.000    0.001    0.000 random.py:334(randint)
        1    0.000    0.000    0.001    0.001 task1.py:220(max_below_zero)
        1    0.000    0.000    0.001    0.001 task1.py:221(<listcomp>)
        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
      101    0.000    0.000    0.000    0.000 {built-in method builtins.len}
      100    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
      142    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}


         6406 function calls in 0.003 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.003    0.003 <string>:1(<module>)
     1000    0.001    0.000    0.001    0.000 random.py:237(_randbelow_with_getrandbits)
     1000    0.001    0.000    0.002    0.000 random.py:290(randrange)
     1000    0.001    0.000    0.002    0.000 random.py:334(randint)
        1    0.000    0.000    0.003    0.003 task1.py:220(max_below_zero)
        1    0.000    0.000    0.003    0.003 task1.py:221(<listcomp>)
        1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
     1001    0.000    0.000    0.000    0.000 {built-in method builtins.len}
     1000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
     1400    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}


         63612 function calls in 0.030 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.030    0.030 <string>:1(<module>)
    10000    0.006    0.000    0.009    0.000 random.py:237(_randbelow_with_getrandbits)
    10000    0.008    0.000    0.018    0.000 random.py:290(randrange)
    10000    0.004    0.000    0.022    0.000 random.py:334(randint)
        1    0.003    0.003    0.030    0.030 task1.py:220(max_below_zero)
        1    0.004    0.004    0.026    0.026 task1.py:221(<listcomp>)
        1    0.000    0.000    0.030    0.030 {built-in method builtins.exec}
    10001    0.001    0.000    0.001    0.000 {built-in method builtins.len}
    10000    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    13606    0.002    0.000    0.002    0.000 {method 'getrandbits' of '_random.Random' objects}


         636386 function calls in 0.333 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.001    0.001    0.333    0.333 <string>:1(<module>)
   100000    0.069    0.000    0.099    0.000 random.py:237(_randbelow_with_getrandbits)
   100000    0.086    0.000    0.185    0.000 random.py:290(randrange)
   100000    0.044    0.000    0.229    0.000 random.py:334(randint)
        1    0.046    0.046    0.331    0.331 task1.py:220(max_below_zero)
        1    0.042    0.042    0.271    0.271 task1.py:221(<listcomp>)
        1    0.000    0.000    0.333    0.333 {built-in method builtins.exec}
   100001    0.015    0.000    0.015    0.000 {built-in method builtins.len}
   100000    0.011    0.000    0.011    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
   136380    0.019    0.000    0.019    0.000 {method 'getrandbits' of '_random.Random' objects}
"""


# Вариант 4
def with_inf(size, min_item, max_item):
    array = [random.randint(min_item, max_item) for _ in range(size)]
    num = float('-inf')
    for i, item in enumerate(array):
        if 0 > item > num:
            num = item
            index = i
    if num != float('-inf'):
        return num, index


print(timeit.timeit('with_inf(100, -750, 750)', number=100, globals=globals()))  # 0.0143157
print(timeit.timeit('with_inf(1_000, -750, 750)', number=100, globals=globals()))  # 0.13228660000000003
print(timeit.timeit('with_inf(10_000, -750, 750)', number=100, globals=globals()))  # 1.4026622
print(timeit.timeit('with_inf(100_000, -750, 750)', number=100, globals=globals()))  # 12.5378877

cProfile.run('with_inf(100, -750, 750)')
cProfile.run('with_inf(1_000, -750, 750)')
cProfile.run('with_inf(10_000, -750, 750)')
cProfile.run('with_inf(100_000, -750, 750)')

# Алгоритм в Варианте №4 имеет O(n) линейную сложность

"""
   534 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
      100    0.000    0.000    0.000    0.000 random.py:237(_randbelow_with_getrandbits)
      100    0.000    0.000    0.000    0.000 random.py:290(randrange)
      100    0.000    0.000    0.000    0.000 random.py:334(randint)
        1    0.000    0.000    0.000    0.000 task1.py:316(with_inf)
        1    0.000    0.000    0.000    0.000 task1.py:317(<listcomp>)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
      100    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
      129    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}


         5387 function calls in 0.002 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.002    0.002 <string>:1(<module>)
     1000    0.000    0.000    0.001    0.000 random.py:237(_randbelow_with_getrandbits)
     1000    0.001    0.000    0.001    0.000 random.py:290(randrange)
     1000    0.000    0.000    0.001    0.000 random.py:334(randint)
        1    0.000    0.000    0.002    0.002 task1.py:316(with_inf)
        1    0.000    0.000    0.002    0.002 task1.py:317(<listcomp>)
        1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
     1000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
     1382    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}


         53651 function calls in 0.018 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.018    0.018 <string>:1(<module>)
    10000    0.004    0.000    0.006    0.000 random.py:237(_randbelow_with_getrandbits)
    10000    0.005    0.000    0.012    0.000 random.py:290(randrange)
    10000    0.003    0.000    0.015    0.000 random.py:334(randint)
        1    0.001    0.001    0.018    0.018 task1.py:316(with_inf)
        1    0.003    0.003    0.017    0.017 task1.py:317(<listcomp>)
        1    0.000    0.000    0.018    0.018 {built-in method builtins.exec}
    10000    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    13646    0.001    0.000    0.001    0.000 {method 'getrandbits' of '_random.Random' objects}


         536815 function calls in 0.175 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.002    0.002    0.175    0.175 <string>:1(<module>)
   100000    0.042    0.000    0.061    0.000 random.py:237(_randbelow_with_getrandbits)
   100000    0.053    0.000    0.114    0.000 random.py:290(randrange)
   100000    0.028    0.000    0.142    0.000 random.py:334(randint)
        1    0.006    0.006    0.173    0.173 task1.py:316(with_inf)
        1    0.025    0.025    0.168    0.168 task1.py:317(<listcomp>)
        1    0.000    0.000    0.175    0.175 {built-in method builtins.exec}
   100000    0.007    0.000    0.007    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
   136810    0.012    0.000    0.012    0.000 {method 'getrandbits' of '_random.Random' objects}
"""

# ВЫВОД:
# Все четыре варианта алгоритмов имееют одинаковую сложность O(n) линейную,
# время выполнения возрастает пропорционально объему обрабатываемых данных.
# На основе данных, полученных с помощью функции timeint - самый быстрый Вариант №2 (с использованиеем фукнции max()).

#Вар.1                  Вар.2                  Вар.3                   Вар.4
# 0.0133051             # 0.0137269            # 0.013298400000000002  # 0.0143157
# 0.1393315             # 0.12708389999999997  # 0.14892480000000002   # 0.13228660000000003
# 1.4489410999999999    # 1.3615561            # 1.6045604             # 1.4026622
# 12.216288800000001    # 11.7607468           # 13.3031404            # 12.5378877

