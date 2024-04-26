import math


# Определение функции f(x) = e^(4.5 * x)
def f(x):
    return math.exp(4.5 * x)


# Определение теоретической первой производной f'(x) = 4.5 * e^(4.5 * x)
def f_prime_theoretical(x):
    return 4.5 * math.exp(4.5 * x)


# Определение теоретической второй производной f''(x) = (4.5)^2 * e^(4.5 * x)
def f_double_prime_theoretical(x):
    return (4.5 ** 2) * math.exp(4.5 * x)


# Функция для генерации данных и вычисления производных
def generate_and_differentiate_formatted(a, h, m):
    # Генерация значений аргумента x
    x_values = [a + i * h for i in range(m + 1)]
    # Вычисление значений функции f(x)
    f_values = [f(x) for x in x_values]

    # Вычисление численных производных
    f_prime_values = []
    f_double_prime_values = []
    for i in range(m + 1):
        # Вычисление численной первой производной
        if i == 0 or i == m:  # Граничные условия для первой производной
            f_prime = None  # Не вычисляем краевые значения численно
        else:
            f_prime = (f_values[i + 1] - f_values[i - 1]) / (2 * h)

        # Вычисление численной второй производной
        if i == 0 or i == m:  # Граничные условия для второй производной
            f_double_prime = None  # Не вычисляем краевые значения численно
        else:
            f_double_prime = (f_values[i + 1] - 2 * f_values[i] + f_values[i - 1]) / (h ** 2)

        f_prime_values.append(f_prime)
        f_double_prime_values.append(f_double_prime)

    # Вывод таблицы значений
    print("{:>8}{:>15}{:>20} | {:>30} {:>20} | {:>30}".format('xi', 'f(xi)', "f'(xi)ЧД", "| f'(xi)Т - f'(xi) ЧД |",
                                                              "f''(xi)ЧД", "| f''(xi)Т - f''(xi) ЧД |"))

    for i, x in enumerate(x_values):
        # Вычисление теоретических значений производных
        f_prime_t = f_prime_theoretical(x)
        f_double_prime_t = f_double_prime_theoretical(x)

        # Получение вычисленных численно значений производных
        f_prime_cd = f_prime_values[i] if f_prime_values[i] is not None else 'N/A'
        f_double_prime_cd = f_double_prime_values[i] if f_double_prime_values[i] is not None else 'N/A'

        # Вычисление погрешностей, если производные вычислены
        prime_error = abs(f_prime_t - f_prime_values[i]) if f_prime_values[i] is not None else 'N/A'
        double_prime_error = abs(f_double_prime_t - f_double_prime_values[i]) if f_double_prime_values[
                                                                                     i] is not None else 'N/A'

        # Вывод строки таблицы
        print(
            f"{x:>8.4f}{f_values[i]:>15.6f}{f_prime_cd:>20}{prime_error:>30}{f_double_prime_cd:>20}{double_prime_error:>30}")


# Ввод пользовательских данных
a = float(input("Введите начальное значение a: "))
h = float(input("Введите шаг h: "))
m = int(input("Введите количество шагов m: "))

# Вызов функции генерации данных и вычисления производных с улучшенным форматированием вывода
generate_and_differentiate_formatted(a, h, m)
