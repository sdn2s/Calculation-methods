import numpy as np
import math
from sympy import diff, symbols, cos, sin

left_border = -8
right_border = 2
eps = 1e-5

def f(x):
    return 10 * math.cos(x) - 0.1 * x**2

def df(x):
    return -10 * math.sin(x) - 0.2 * x

def tabulation_approach(a, b, step):
    intervals = []
    sign_changes = 0

    current_x = a
    while current_x <= b:
        current_y = f(current_x)
        next_x = current_x + step
        next_y = f(next_x)

        if current_y * next_y <= 0:
            intervals.append((current_x, next_x))
            sign_changes += 1

        current_x = next_x

    print(f"Отрезки изменения знака: {', '.join(map(lambda interval: f'[{interval[0]:.4f}, {interval[1]:.4f}]', intervals))}")
    print(f"Количество отрезков изменения знака: {sign_changes}")

def bisection(a, b, n, eps):
    assert a!=0, 'a равно 0'
    assert b!=0, 'b равно 0'
    count = 0
    setka = np.linspace(a, b, n)
    for x, y in zip(setka, setka[1:]):
        if f(x) * f(y) > 0:
            continue
        root = None
        while abs(f(y) - f(x)) > eps:
            mid = (y + x) / 2
            if f(mid) == 0 or f(mid) < eps:
                root = mid
                break
            elif (f(mid) * f(x)) < 0:
                y = mid
            else:
                x = mid
            count += 1
        if root:
            yield root
    print("Количество шагов для достижения точности epsilon:", count)

def newton_method(initial_guess, eps):
    x0 = initial_guess
    count = 0

    while True:
        x1 = x0 - f(x0) / df(x0)
        count += 1

        if abs(x1 - x0) < eps:
            break

        x0 = x1

    return x1, count

def modified_newton(f, df, x0, eps=1e-5, max_iter=1000):
    x = x0
    iteration = 0

    while True:
        x_new = x - f(x) / df(x0)
        iteration += 1
        if abs(x_new - x) < eps or iteration >= max_iter:
            break

        x = x_new

    return x_new, iteration

def secant_method(f, x0, x1, eps=1e-5, max_iter=100):
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
print(f"Параметры:\nЛевая граница: {left_border}\nПравая граница: {right_border}\nТочность: {eps}")
print("Метод бисекции:")
tabulation_approach(left_border, right_border, 0.1)
res = list(bisection(left_border, right_border, 1000, 0.00001))
print('Корни по методу бисекции находятся в точках:')
print(', '.join(map(lambda x: f'{x:.4f}', res)))
print("Метод Ньютона:")
initial_guess = (left_border + right_border) / 2
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
