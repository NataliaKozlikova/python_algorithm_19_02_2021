"""
Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
Ссылка на алгоритм (блок-схему) https://viewer.diagrams.net/?highlight=0000ff&edit=https%3A%2F%2Fapp.diagrams.net%2F%23G13ai52hkwVWhmCDtvmEf9pz9rY3atcvtY&layers=1&nav=1#G13ai52hkwVWhmCDtvmEf9pz9rY3atcvtY
"""

a = int(input("Введите трехзначное число:\n >> "))
b = a // 100
c = (a - b * 100) // 10
d = a - b * 100 - c * 10

a = b + c + d
print(f'Сумма цифр трехзначного числа: {a}')

a = b * c * d
print(f'Произведение цифр трехзначного числа: {a}')
