import numpy as np
import math
from sympy import diff, symbols, cos, sin
left_border = -8
right_border = 2
eps = 1e-5
# определение функция
def f(x):
    return 10 * math.cos(x) - 0.1 * x**2
# определение производной
def df(x):
    return -10 * math.sin(x) - 0.2 * x
# процедура отделения корней
def tabulation_approach(a, b, step):
    intervals = []  # Список для хранения отрезков изменения знака
    sign_changes = 0 # счетчик изменений знака

    current_x = a
    while current_x <= b:
        current_y = f(current_x) # Значение функции в текущей точке
        next_x = current_x + step # Переход к следующей точке с шагом step
        next_y = f(next_x) # Значение функции в следующей точке

        if current_y * next_y <= 0:  # Проверка на изменение знака
            intervals.append((current_x, next_x))
            sign_changes += 1

        current_x = next_x # Переопределение текущей точки для следующей итерации

    print(f"Отрезки изменения знака: {', '.join(map(lambda interval: f'[{interval[0]:.4f}, {interval[1]:.4f}]', intervals))}")
    print(f"Количество отрезков изменения знака: {sign_changes}")
# Метод бисекции
def bisection (a,b,n, eps): # отрезок от a до b делим на n частей, погрешность eps
    assert a!=0,  'a равно 0'
    assert b!=0, 'b равно 0'
    count = 0 # счетчик количества итераций для достижения точности epsilon
    # сначала отделим корни
    setka=np.linspace(a, b, n)
    # далее уточним корни
    for x,y in zip(setka, setka[1:]):
        if f(x) * f(y) > 0: # если на отрезке нет корня, смотрим следующий
            continue
        root = None
        while ( abs(f(y)-f(x)) )>eps:     # пока отрезок больше заданной погрешности, выполняем нижестоящие операции:
            mid = (y+x)/2                   # получаем середину отрезка
            if f(mid) == 0 or f(mid)<eps:    # если функция в середине отрезка равну нулю или меньше погрешности:
                root = mid                  # корень равень серединному значению
                break
            elif (f(mid) * f(x)) < 0:       # иначе если произведение функции в середине отрезка на функцию в т. а <0
                y = mid                     # серединой становится точка b
            else:
                x = mid                     #в другом случае - точка а
            count += 1
        if root:
            yield root
    print("Количество шагов для достижения точности epsilon:", count)
# Реализация метода Ньютона для нахождения корня функции
def newton_method(initial_guess, eps):
    x0 = initial_guess # начальное предположение
    count = 0 # счетчик итераций

    while True:
        x1 = x0 - f(x0) / df(x0) # основная формула метода Ньютона
        count += 1

        if abs(x1 - x0) < eps: # проверка точности
            break

        x0 = x1 # изменение предположения

    return x1, count
# Модифицированный метод Ньютона
def modified_newton(f, df, x0, eps = 1e-5, max_iter=1000):
    x = x0
    iteration = 0

    while True:
        x_new = x - f(x) / df(x0) # обновление значения x  по формуле Ньютона
        iteration += 1
        # проверка условия сходимости или достижения максимального количества итераций
        if abs(x_new - x) < eps or iteration >= max_iter:
            break

        x = x_new

    return x_new, iteration
def secant_method(f, x0, x1, eps = 1e-5, max_iter=100):
    iterations = 0

    while iterations < max_iter:
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))

        if abs(x2 - x1) < eps:
            return x2, iterations

        x0 = x1
        x1 = x2
        iterations += 1

    raise Exception("Не удалось найти корень методом секущих")
print("Функция f(x): 10 * cos(x) - 0.1 * x**2")
print("Параметры:\nЛевая граница: {}\nПравая граница: {}\nТочность: {}".format(left_border, right_border, eps))
print("Метод бисекции:")
tabulation_approach(-8, 2, 0.1)
res = list(bisection(-8,2,1000, 0.00001))
print('Корни по методу бисекции находятся в точках:')
print(', '.join(map(lambda x: f'{x:.4f}', res)))
print("Метод Ньютона:")
initial_guess = (left_border+right_border)/2  # начальное предположение

root, iterations = newton_method(initial_guess, eps)

print(f"Корень методом Ньютона: {root:.6f}")
print(f"Количество итераций: {iterations}")

print("Модифицированный метод Ньютона:")
x0 = 1.5
solution, iterations = modified_newton(f, df, x0)

print("Корень: {:.7f}".format(solution))
print("Количество итераций:", iterations)
print("Метод секущих: ")
x0 = 1
x1 = 2

solution_secant, iterations_secant = secant_method(f, x0, x1)
print("Корень уравнения {:.7f}:".format(solution_secant))
print("Количество итераций:", iterations_secant)


