# Завдання: Визначте список чисел і обчисліть їх суму.

numbers_list = [1, 3, 15, 7, 9, 11, 33, 1, 12]

# Варіант 1
# total = sum(numbers_list)
# print (f"Total of number_list: {total}")

# Варіант 2
total = 0
for number in numbers_list:
    total = total + number
print(f"Total of number_list: {total}")