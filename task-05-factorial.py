# Завдання: Обчисліть факторіал заданого числа.
# Факторіал числа — це добуток всіх цілих чисел від 1 до вказаного числа. 
# Наприклад, факторіал числа 6 дорівнює 1*2*3*4*5*6 = 720

num = 6
total = 1

while num > 1:
    total = total * num
    num -= 1
   
print(f"Factorial: ", total)