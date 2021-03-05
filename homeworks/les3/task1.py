"""
1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
"""

result = {}
for num in range(2, 10):
    result[num] = []
    for i in range(2, 100):
        if i % num == 0:
            result[num].append(i)
    print(f'{num} кратны - {len(result[num])} чисел: {result[num]}.')
