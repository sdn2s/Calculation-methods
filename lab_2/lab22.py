from math import *
import pandas as pd
import numpy as np
import time
import math


def f(x):  # Функция
    return math.exp(-x) - (x**2) / 2


def sort(sp, x):  # Сортировка списка по x
    k = 1
    while k == 1:
        k = 0
        for i in range(len(sp) - 1):
            if abs(sp[i] - x) > abs(sp[i + 1] - x):
                k = sp[i]
                sp[i] = sp[i + 1]
                sp[i + 1] = k
                k = 1


def Table_print(sp):  # Вывод на экран таблицы значений
    print("    x    |   f(x)   ")
    table = pd.Series([f(i) for i in nodes], nodes)
    print(table)
    print('\n')


def Diff_function(sp):  # Функция возвращает разделенную разность порядка размера списка sp
    if len(sp) == 2:
        return (f(sp[1]) - f(sp[0])) / (sp[1] - sp[0])
    else:
        return (Diff_function(sp[1:]) - Diff_function(sp[:-1])) / (sp[-1] - sp[0])


def Interpolation_function_newton(x, sp_nod):  # Возвращает значение в точке интерполирования x в форме Ньютона
    mul = 1
    if len(sp_nod) == 1:
        return f(sp_nod[0])
    else:
        for i in range(len(sp_nod)-1):
            mul *= x - sp_nod[i]
        return Interpolation_function_newton(x, sp_nod[:-1]) + (Diff_function(sp_nod) * mul)


def Interpolation_function_lagrange(x, sp_nod, kol):  # Возвращает значение в точке интерполирования x в форме Лагранжа
    s = 0
    for i in range(kol + 1):
        mul1, mul2 = 1, 1
        for j in range(kol + 1):
            if j != i:
                mul1 *= x - sp_nod[j]
                mul2 *= sp_nod[i] - sp_nod[j]
        s += (mul1 / mul2) * f(sp_nod[i])
    return s


m = 10  # Количество узлов - 1
a, b = 1, 12  # Промежуток [a, b]
nodes = [a + i * (b - a) / m for i in range(m + 1)]  # Список значений

while True:
    differences = []
    print("Таблица значений:\n")
    Table_print(nodes)

    print("Введите точку интерполирования: ")
    x0 = float(input())  # Точка интерполирования

    while True:
        print(f"Введите n < {m}: ")
        n = int(input())
        if n <= m:
            break
        else:
            print("Введено недопустимое значение n")

    sort(nodes, x0)  # Сортировка nodes по x

    print(f"Число значений: {m + 1}\n"
          f"Точка интерполирования: {x0}\n"
          f"Степень многочлена: {n}\n"
          "Таблица отсортированных значений:\n")
    Table_print(nodes)

    # -Представление в форме Ньютона #

    P_newton = Interpolation_function_newton(x0, nodes[:n+1])  # Значение в точке интерполировани

    print(f"P_n(x) = {P_newton}\n"
          f"Фактическая погрешность: {abs(f(x0) - P_newton)}\n")

    # Представление в форме Лагранжа #

    print("Представление в форме Лагранжа:\n")
    P_lagrange = Interpolation_function_lagrange(x0, nodes, n)
    print(f"P_n(x) = {P_lagrange}\n"
          f"Фактическая погрешность: {abs(f(x0) - P_lagrange)}\n")

    print("Хотите ввести новые значения x и n?\n"
          "1. Да\n"
          "2. Нет\n")
    if int(input()) == 2:
        break