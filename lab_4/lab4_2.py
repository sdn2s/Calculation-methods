import math

def f(x):
    """ Пример функции, которую мы интегрируем: f(x) = x^2 """
    return x**2

def analytical_integral(a, b):
    """ Аналитическое решение интеграла функции f(x) = x^2 """
    return (b**3)/3 - (a**3)/3

def left_rectangle(a, b, m, func):
    """ Составная квадратурная формула левых прямоугольников """
    h = (b - a) / m
    return sum(func(a + i * h) * h for i in range(m))

def right_rectangle(a, b, m, func):
    """ Составная квадратурная формула правых прямоугольников """
    h = (b - a) / m
    return sum(func(a + (i + 1) * h) * h for i in range(m))

def midpoint_rectangle(a, b, m, func):
    """ Составная квадратурная формула средних прямоугольников """
    h = (b - a) / m
    return sum(func(a + (i + 0.5) * h) * h for i in range(m))

def trapezoidal(a, b, m, func):
    """ Составная квадратурная формула трапеций """
    h = (b - a) / m
    return (h / 2) * (func(a) + func(b) + 2 * sum(func(a + i * h) for i in range(1, m)))

def simpson(a, b, m, func):
    """ Составная квадратурная формула Симпсона """
    if m % 2 != 0:
        m += 1  # Делаем m чётным, если это не так
    h = (b - a) / m
    total = func(a) + func(b)
    # Вклады точек внутри интервалов
    for i in range(1, m):
        if i % 2 == 0:  # Для чётных индексов
            total += 2 * func(a + i * h)
        else:  # Для нечётных индексов
            total += 4 * func(a + i * h)
    return (h / 3) * total

# Параметры задачи
a = float(input("Введите нижний предел интегрирования A: "))
b = float(input("Введите верхний предел интегрирования B: "))
m = int(input("Введите количество промежутков деления m: "))

# Вычисления
J = analytical_integral(a, b)
methods = [left_rectangle, right_rectangle, midpoint_rectangle, trapezoidal, simpson]
method_names = ["Левых прямоугольников", "Правых прямоугольников", "Средних прямоугольников", "Трапеций", "Симпсона"]
print(f"Аналитический результат: J = {J:.6f}")
for method, name in zip(methods, method_names):
    J_h = method(a, b, m, f)
    error = abs(J - J_h)
    print(f"{name}: J(h) = {J_h:.6f}, |J - J(h)| = {error:.6f}")
