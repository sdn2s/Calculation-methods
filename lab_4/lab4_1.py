import math

# Определение функций многочленов
def f0(x):
    return 1 # Константа

def f1(x):
    return 2 * x + 3 # Линейная функция

def f2(x):
    return x**2 - 4 * x + 4 # Квадратичная функция

def f3(x):
    return x**3 - 3 * x**2 + 3 * x - 1 # Кубическая функция

# Аналитическое решение интеграла для выбранной функции
def analytical_integral_poly(func, a, b):
    if func == f0:
        return b - a # Интеграл от константы
    elif func == f1:
        return (2*b**2)/2 + 3*b - (2*a**2)/2 - 3*a # Интеграл от линейной функции
    elif func == f2:
        return (b**3)/3 - 4*(b**2)/2 + 4*b - ((a**3)/3 - 4*(a**2)/2 + 4*a) # Интеграл от квадратичной функции
    elif func == f3:
        return (b**4)/4 - 3*(b**3)/3 + 3*(b**2)/2 - b - ((a**4)/4 - 3*(a**3)/3 + 3*(a**2)/2 - a) # Интеграл от кубической функции

# Квадратурные методы

# Простые квадратурные методы
def left_rectangle(a, b, func):
    h = b - a
    return func(a) * h

def right_rectangle(a, b, func):
    h = b - a
    return func(b) * h

def midpoint_rectangle(a, b, func):
    h = b - a
    return func((a + b) / 2) * h

def trapezoidal(a, b, func):
    h = b - a
    return (h / 2) * (func(a) + func(b))

def simpson(a, b, func):
    h = b - a
    return (h / 3) * (func(a) + 4 * func((a + b) / 2) + func(b))

def three_eighths(a, b, func):
    """ Простая квадратурная формула 3/8 """
    h = (b - a) / 3
    x1 = a + h
    x2 = a + 2 * h
    return (3 * h / 8) * (func(a) + 3 * func(x1) + 3 * func(x2) + func(b))

# Ввод параметров и выбор функции
a = float(input("Введите нижний предел интегрирования a: "))
b = float(input("Введите верхний предел интегрирования b: "))
function_choice = int(input("Выберите функцию (0 - константа, 1 - линейная, 2 - квадратичная, 3 - кубическая): "))
functions = [f0, f1, f2, f3]
selected_function = functions[function_choice]

# Расчёт и вывод результатов
J = analytical_integral_poly(selected_function, a, b)
methods = [left_rectangle, right_rectangle, midpoint_rectangle, trapezoidal, simpson, three_eighths]
method_names = ["Левые прямоугольники", "Правые прямоугольники", "Средние прямоугольники", "Трапеции", "Симпсон", "3/8"]
print(f"Аналитический результат: J = {J}")
for method, name in zip(methods, method_names):
    result = method(a, b, selected_function)
    error = abs(result - J)
    print(f"{name}: {result}, Погрешность: {error}")
