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
    s_ch = 0 # счетчик изменений знака

    c_x = a
    while c_x <= b:
        c_y = f(c_x) # Значение функции в текущей точке
        n_x = c_x + step # Переход к следующей точке с шагом step
        n_y = f(n_x) # Значение функции в следующей точке

        if c_y * n_y <= 0:  # Проверка на изменение знака
            intervals.append((c_x, n_x))
            s_ch += 1

        c_x = n_x # Переопределение текущей точки для следующей итерации

    print(f"Отрезки изменения знака: {', '.join(map(lambda interval: f'[{interval[0]:.4f}, {interval[1]:.4f}]', intervals))}")
    print(f"Количество отрезков изменения знака: {s_ch}")
# Метод бисекции
def bisection(a, b, n, eps):
    assert a != 0, 'a равно 0'
    assert b != 0, 'b равно 0'
    count = 0  # счетчик количества итераций для достижения точности epsilon
    # отделение корней
    s = np.linspace(a, b, n)
    roots = []
    # уточнение корней
    for x, y in zip(s, s[1:]):
        if f(x) * f(y) > 0:  # если на отрезке нет корня, смотрим следующий
            continue
        root = None
        while abs(f(y) - f(x)) > eps:  # пока отрезок больше заданной погрешности:
            mid = (y + x) / 2  # получаем середину отрезка
            if f(mid) == 0 or f(mid) < eps:  # если функция в середине отрезка равна нулю или меньше погрешности:
                root = mid  # корень равен среднему значению
                break
            elif f(mid) * f(x) < 0:  # выбор новой середины
                y = mid  # серединой становится точка b
            else:
                x = mid  # иначе точка a
            count += 1
        if root:
            roots.append(root)
    print("Количество шагов для достижения точности epsilon:", count)
    return roots
# Реализация метода Ньютона для нахождения корня функции
def newton(initial_guess, eps):
    x0 = initial_guess # начальное предположение
    count = 0 # счетчик итераций

    while True:
        x = x0 - f(x0) / df(x0) # основная формула метода Ньютона

        if abs(x - x0) < eps: # проверка точности
            return x, count

        x0 = x # изменение предположения
        count += 1

# Модифицированный метод Ньютона
def modified_newton_method(f, df, x0, alpha=1.0, eps=1e-5):
    x = x0
    iterations = 0

    while True:
        x_n = x - alpha * f(x) / df(x)

        if abs(x_n - x) < eps:
            return x_n, iterations

        x = x_n
        iterations += 1

def secant_method(f, a, b, eps = 1e-5):
    iterations = 0
    # Вычисление нового приближения x2 с использованием метода секущих
    while True:
        x = b - f(b) * (b - a) / (f(b) - f(a))
        # Проверка на достижение требуемой точности
        if abs(x - b) < eps:
            return x, iterations # Если точность достигнута, возвращаем найденное значение и количество итераций

        a = b
        b = x
        iterations += 1

print("Функция f(x): 10 * cos(x) - 0.1 * x**2")
print("Параметры:\nЛевая граница: {}\nПравая граница: {}\nТочность: {}".format(left_border, right_border, eps))

print("Метод бисекции:")
tabulation_approach(-8, 2, 0.1)
res = list(bisection(-8,2,1000, 0.00001))
print('Корни по методу бисекции находятся в точках:')
print(', '.join(map(lambda x: f'{x:.4f}', res)))

print("Метод Ньютона:")
initial_guess = (left_border+right_border)/2  # начальное предположение
root, iterations = newton(initial_guess, eps)
print(f"Корень методом Ньютона: {root:.6f}")
print(f"Количество итераций: {iterations}")

print("Модифицированный метод Ньютона:")
x0 = 1.5
solution, iterations = modified_newton_method(f, df, x0)
print("Корень: {:.7f}".format(solution))
print("Количество итераций:", iterations)

print("Метод секущих: ")
a = 1
b = 2
solution_secant, iterations_secant = secant_method(f, a, b)
print("Корень уравнения {:.7f}:".format(solution_secant))
print("Количество итераций:", iterations_secant)


