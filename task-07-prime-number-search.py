# Завдання: Знайдіть всі прості числа в заданому діапазоні.
# Прості числа - це числа, які ділять тільки на 1 та на саме себе без остачі
# Наприклад, 2 ділиться на 1 і 2, 3 ділиться на 1 і 3, 5 ділиться на 1 і 5

numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# for number in numbers_list:
#     print(number)
#     if number % 

a = 13
while a > 1:
    b = a
    d = 1
    c = a - d
    if b % (a - d) != 0:
        d += 1
    else:
        print(a)