"""
По введенным пользователем координатам двух точек вывести уравнение прямой вида y = kx + b, проходящей через эти точки.
Ссылка на алгоритм (блок-схему) https://viewer.diagrams.net/?highlight=0000ff&edit=https%3A%2F%2Fapp.diagrams.net%2F%23G13ai52hkwVWhmCDtvmEf9
"""

print('Введите координаты точки А (x1, y1):')
x1 = float(input("\tx1 = "))
y1 = float(input("\ty1 = "))

print('Введите координаты точки B (x2, y2):')
x2 = float(input("\tx2 = "))
y2 = float(input("\ty2 = "))

k = round(((y1 - y2) / (x1 - x2)), 2)
b = round((y2 - k * x2), 2)

print(f'Уравнение прямой, проходящей через точки А ({x1}, {y1}) и B ({x2}, {y2}):\ny = {k} * x + {b}')
