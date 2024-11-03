# Завдання: Виведіть всі парні числа від 1 до 50.

a = 1
b = 50
even_numbers = []

while a <= 50:
    if a % 2 == 0:
        even_numbers.append(a)
        a += 1
    else:
        a += 1
        
print(even_numbers)