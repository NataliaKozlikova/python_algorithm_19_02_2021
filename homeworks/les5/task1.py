"""Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа) для
каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести
наименования предприятий, чья прибыль выше среднего и ниже среднего. """

from collections import namedtuple

Company = namedtuple('Company', ['profit_1q', 'profit_2q', 'profit_3q', 'profit_4q'])

n = int(input('Введите количество предприятий: '))

companies = {}

for i in range(n):
    name = input('Введите название ' + str(i + 1) + ' предприятия: ')
    profit_1q = int(input('Введите прибыль за 1-й квартал: '))
    profit_2q = int(input('Введите прибыль за 2-й квартал: '))
    profit_3q = int(input('Введите прибыль за 3-й квартал: '))
    profit_4q = int(input('Введите прибыль за 4-й квартал: '))
    companies[name] = Company(profit_1q, profit_2q, profit_3q, profit_4q)

total_profit = ()

for name, profit in companies.items():
    print(f'Предприятие: {name} прибыль за год - {sum(profit)}')
    total_profit += profit

avg_total_profit = sum(total_profit) / len(companies)
print(f'Средняя прибыль за год для всех предприятий {avg_total_profit}')

print('Предприятия c прибылью выше среднего:')

for name, profit in companies.items():
    if sum(profit) > avg_total_profit:
        print(f'{name} - {sum(profit)}')

print('Предприятия с прибылью ниже среднего:')

for name, profit in companies.items():
    if sum(profit) < avg_total_profit:
        print(f'{name} - {sum(profit)}')
