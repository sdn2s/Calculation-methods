import math
import random

# Функция вариант №7
def f(x):
    return math.exp(-x) - (x**2) / 2

# Функция для генерации узлов и вывода таблицы значений
def generate_nodes_and_print_table(alpha, m_plus_1, b, f):
    if m_plus_1 <= (b - alpha):
        # 1. Случайные узлы
        nodes = sorted(random.sample([i / 10 for i in range(int(alpha * 10), int(b * 10))], m_plus_1))
    else:
        # 2. Узлы по формуле с шагом h для первых m элементов
        h = (b - alpha) / (m_plus_1 - 1)
        nodes = [alpha + j * h for j in range(m_plus_1 - 1)]
        # Добавление последнего узла
        nodes.append(b)

    # Создание и вывод таблицы значений
    print("j\tzj\t\tf(zj)")
    print("-" * 25)

    # Вывод значений узлов и соответствующих им значений функции
    for j, zj in enumerate(nodes):
        fj = f(zj)
        print(f"{j}\t{zj:.4f}\t{fj:.4f}")

    return nodes

# Функция интерполяции Лагранжа
def lagranz(x, y, t):
    z = 0
    # Цикл по всем узлам
    for j in range(len(y)):
        p1 = 1
        p2 = 1
        # Цикл по всем узлам для вычисления числителя и знаменателя
        for i in range(len(x)):
            if i == j:
                # Условие для текущего узла, p1 и p2 остаются 1
                p1 = p1 * 1
                p2 = p2 * 1
            else:
                # Обновление числителя и знаменателя
                p1 = p1 * (t - x[i])
                p2 = p2 * (x[j] - x[i])
        # Обновление значения интерполяционного многочлена для текущего узла
        z = z + y[j] * p1 / p2
    # Возвращение значения интерполяционного многочлена в точке t
    return z

# Функция для вычисления разделенных разностей
def divided_differences(x, y):
    # Получение количества узлов
    n = len(x)
    # Инициализация таблицы разделенных разностей
    f = [[0] * n for _ in range(n)]

    # Заполнение первого столбца таблицы значениями функции в узлах
    for i in range(n):
        f[i][0] = y[i]

    # Заполнение остальных столбцов таблицы
    for j in range(1, n):
        for i in range(n - j):
            # Вычисление разделенной разности
            f[i][j] = (f[i + 1][j - 1] - f[i][j - 1]) / (x[i + j] - x[i])
    # Возвращение значений первого столбца таблицы
    return [f[0][j] for j in range(n)]

# Параметры задачи
alpha = 0.2
m_plus_1 = 11
b = 0.7

# Вызов функции для генерации узлов и вывода таблицы значений
nodes = generate_nodes_and_print_table(alpha, m_plus_1, b, f)

# Построение таблицы разделенных разностей
differences_table = divided_differences(nodes, [f(xi) for xi in nodes])

# Введенные пользователем значения
t = float(input("Введите значение x для интерполяции: "))
n = int(input("Введите степень интерполяционного многочлена n (n ≤ m): "))

# Сортировка узлов по удалению от точки интерполирования t
sorted_nodes = sorted(nodes, key=lambda z: abs(z - t))

# Выбор первых (n+1) отсортированных узлов
selected_nodes = sorted_nodes[:n + 1]

# Построение интерполяционного многочлена в форме Ньютона
def newton_interpolation(x, differences, t):
    # Инициализация значения многочлена для первого узла
    result = differences[0]
    # Инициализация переменной для хранения произведения (t - x[i-1])
    product_term = 1
    # Цикл по разделенным разностям, начиная со второго узла
    for i in range(1, len(differences)):
        product_term *= (t - x[i - 1])
        # Обновление значения многочлена с учетом новой разделенной разности
        result += differences[i] * product_term
    # Возвращение значения интерполяционного многочлена в точке t
    return result

# Вычисление фактической погрешности для Лагранжа
interpolation_result_lagrange = lagranz(selected_nodes, [f(xi) for xi in selected_nodes], t)
'''interpolation_result_lagrange: 
Это переменная, в которой будет храниться результат вычисления интерполяционного многочлена Лагранжа в точке t 
с использованием выбранных узлов selected_nodes.
lagranz(selected_nodes, [f(xi) for xi in selected_nodes], t): 
Это вызов функции lagranz, которая принимает выбранные узлы selected_nodes, 
соответствующие значения функции в этих узлах [f(xi) for xi in selected_nodes] 
и точку интерполяции t. Функция возвращает значение интерполяционного многочлена Лагранжа в точке t.'''
actual_error_lagrange = abs(f(t) - interpolation_result_lagrange)

# Вычисление фактической погрешности для Ньютона
interpolation_result_newton = newton_interpolation(selected_nodes, differences_table[:n + 1], t)
'''interpolation_result_newton: 
Это переменная, в которой будет храниться результат вычисления интерполяционного многочлена Ньютона в точке t 
с использованием выбранных узлов selected_nodes 
и таблицы разделенных разностей differences_table.
newton_interpolation(selected_nodes, differences_table[:n + 1], t): 
Это вызов функции newton_interpolation, которая принимает выбранные узлы selected_nodes, 
разделенные разности для построения интерполяционного многочлена differences_table[:n + 1] 
(только необходимые для степени n), и точку интерполяции t. 
Функция возвращает значение интерполяционного многочлена Ньютона в точке t.'''
actual_error_newton = abs(f(t) - interpolation_result_newton)

# Вывод результатов для Лагранжа
print("\nИнтерполяция Лагранжа:")
print(f"Выбранные узлы: {selected_nodes}")
print(f"Интерполяционный многочлен в форме Лагранжа в точке x: PnL({t}) = {interpolation_result_lagrange}")
print(f"Фактическая погрешность Лагранжа: efn({t}) = {actual_error_lagrange}")

# Вывод результатов для Ньютона
print("\nИнтерполяция Ньютона:")
print(f"Выбранные узлы: {selected_nodes}")
print(f"Интерполяционный многочлен в форме Ньютона в точке x: PnN({t}) = {interpolation_result_newton}")
print(f"Фактическая погрешность Ньютона: efn({t}) = {actual_error_newton}")

