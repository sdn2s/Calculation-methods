import math
import random


# Определение исходной функции f(x)
def f(x):
    return math.exp(-x) - (x ** 2) / 2


# Генерация исходных данных для интерполяции
def generate_data(a, b, m):
    # Шаг между точками
    h = (b - a) / m
    # Генерация значений аргумента x
    x_values = [a + i * h for i in range(m + 1)]
    # Вычисление значений функции f(x)
    f_values = [f(x) for x in x_values]
    return x_values, f_values


# Функция для вывода таблицы значений
def print_table(x_values, f_values):
    print("i\t xi\t\t f(xi)")
    print("-" * 30)
    for i, (xi, fxi) in enumerate(zip(x_values, f_values)):
        print(f"{i}\t {xi:.4f}\t {fxi:.4f}")


# Параметры для примера
a = 0
b = 7
m = 11

# Генерация данных для заданных параметров
x_values, f_values = generate_data(a, b, m)
# Вывод таблицы значений
print_table(x_values, f_values)


# Обратная интерполяция: поиск x по заданному F
def inverse_interpolation(x_vals, y_vals, F, n):
    # Вложенная функция для интерполяции методом Лагранжа
    def lagrange(x, y, target):
        n = len(x)
        result = 0
        for i in range(n):
            term = y[i]
            for j in range(n):
                if i != j:
                    term *= (target - x[j]) / (x[i] - x[j])
            result += term
        return result

    # Сортировка пар значений по близости к F
    sorted_pairs = sorted(zip(y_vals, x_vals), key=lambda pair: abs(pair[0] - F))
    # Выбор n + 1 ближайших точек к F
    selected_pairs = sorted_pairs[:n + 1]
    selected_y, selected_x = zip(*selected_pairs)
    # Интерполяция Лагранжем для получения приближенного x
    approx_x = lagrange(selected_y, selected_x, F)
    return approx_x


# Ввод пользователем значения F и степени интерполяционного многочлена n
F_user = float(input("Введите значение F для нахождения x: "))
n_user = int(input("Введите степень интерполяционного многочлена n (n ≤ m): "))

# Выполнение обратной интерполяции
approximated_x = inverse_interpolation(f_values, x_values, F_user, n_user)
residual = abs(f(approximated_x) - F_user)

# Вывод результатов
print(f"Приближенное значение x для F = {F_user}: x ≈ {approximated_x:.4f}")
print(f"Модуль невязки: |f(x) - F| = {residual:.4f}")
