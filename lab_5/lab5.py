from math import *
import pandas as pd

# Вывод заголовка
print("КФ Гаусса, ее узлы и коэффициенты\n"
      "по составным квадратурным формулам\n")

# Задание функций
def f(x):
    return sin(x) / x

def f_3(x):
    return x ** 3 + 5 * x ** 2

def f_7(x):
    return x ** 7 + 4 * x ** 2 - 2 * x

# Рекурсивная функция для вычисления многочлена Лежандра
def legendre_fun(x, n):
    if n == 0:
        return 1
    if n == 1:
        return x
    return (2 * n - 1) / n * legendre_fun(x, n - 1) * x - (n - 1) / n * legendre_fun(x, n - 2)

# Функция для вывода таблицы
def Table_print(sp):
    table = pd.DataFrame(sp)
    print(table.to_string(index=False))
    print('\n')

# Функция для разделения корней многочлена Лежандра на интервалы
def Sepofroots(a, b, n):
    sp = []
    h = (b - a) / 1000
    a_0 = a
    b_0 = a_0 + h
    while b_0 <= b:
        y_0 = legendre_fun(a_0, n)
        y_1 = legendre_fun(b_0, n)
        if y_0 * y_1 <= 0:
            sp.append((a_0, b_0))
        a_0 = b_0
        b_0 = a_0 + h
    return sp

# Функция для метода бисекции (половинного деления)
def Halfdiv(sp, ep, n):
    sp_coef = {'Узел': [], 'Коэффициент': []}
    for inter in sp:
        m = 0
        a = inter[0]
        b = inter[1]
        while b - a >= 2 * ep:
            c = (a + b) / 2
            if legendre_fun(a, n) * legendre_fun(c, n) <= 0:
                b = c
            else:
                a = c
            m += 1
        x = (a + b) / 2
        s = (2 * (1 - x ** 2)) / (n * legendre_fun(x, n - 1)) ** 2
        sp_coef['Узел'].append(x)
        sp_coef['Коэффициент'].append(s)
    return sp_coef

a = -1
b = 1
ep = 10 ** (-12)

# Главный цикл для различных степеней полиномов
for i in range(1, 9):
    print(f'\nУзлы и коэффициенты КФ Гаусса для N = {i}')
    segm = Sepofroots(a, b, i)
    if i == 1:
        nodes_1 = Halfdiv(segm, ep, i)
        Table_print(nodes_1)
    if i == 2:
        nodes_2 = Halfdiv(segm, ep, i)
        Table_print(nodes_2)
    if i == 3:
        nodes_3 = Halfdiv(segm, ep, i)
        Table_print(nodes_3)
    if i == 4:
        nodes_4 = Halfdiv(segm, ep, i)
        Table_print(nodes_4)
    if i == 5:
        nodes_5 = Halfdiv(segm, ep, i)
        Table_print(nodes_5)
    if i == 6:
        nodes_6 = Halfdiv(segm, ep, i)
        Table_print(nodes_6)
    if i == 7:
        nodes_7 = Halfdiv(segm, ep, i)
        Table_print(nodes_7)
    if i == 8:
        nodes_8 = Halfdiv(segm, ep, i)
        Table_print(nodes_8)

# Проверка результатов на многочленах
print('\n--------------------Проверка----------------------')
print('\nПроверка на многочлене x^3 + 5x^2 (N = 2 на отрезке [-1, 1])')
sum_2 = 0
for i in range(0, 2):
    sum_2 += nodes_2['Коэффициент'][i] * f_3(nodes_2['Узел'][i])
print('Точное значение интеграла: 10/3')
print('Значение через КФ Гаусса:', sum_2)
print('Абсолютная фактическая погрешность:', abs(10 / 3 - sum_2))

print('\nПроверка на многочлене x^7 + 4x^2 - 2x (N = 4 на отрезке [-1, 1])')
sum_4 = 0
for i in range(0, 4):
    sum_4 += nodes_4['Коэффициент'][i] * f_7(nodes_4['Узел'][i])
print('Точное значение интеграла: 8/3')
print('Значение через КФ Гаусса:', sum_4)
print('Абсолютная фактическая погрешность:', abs(8 / 3 - sum_4))
print('\n--------------------------------------------------\n')

# Ввод пользователем новых границ и вычисление интегралов
while True:
    A_main = int(input('Введите нижнюю границу: '))
    B_main = int(input('Введите верхнюю границу: '))

    print(f'\n Для N = 2')
    coeff_2 = {'Узел': [], 'Коэффициент': []}
    for i in range(0, 2):
        coeff_2['Узел'].append(nodes_2['Узел'][i] * (B_main - A_main) / 2 + (B_main + A_main) / 2)
        coeff_2['Коэффициент'].append((B_main - A_main) / 2 * nodes_2['Коэффициент'][i])
    print('Преобразованная таблица')
    Table_print(coeff_2)
    val = 0
    for i in range(0, 2):
        val += coeff_2['Коэффициент'][i] * f(coeff_2['Узел'][i])
    print(f'Значение определнного интеграла через КФ Гаусса:', val)

    # Повторение того же для других степеней
    # Сокращено, поскольку аналогично предыдущему блоку кода

    print("Ввести новые значения?\n"
          "1. Да\n"
          "2. Нет")
    n = int(input())
    if n == 2:
        break
