# Визначення днів тижня:
# Завдання: Створіть програму, яка встановлює номер дня тижня 
# і виводить назву відповідного дня тижня. 
# Якщо номер дня недійсний (менше 1 або більше 7), виведіть повідомлення про помилку.

numbers_list = [5, 3, 1, 0, 8, 4, 7]

for number in numbers_list:
    if number == 1:
        print("Monday")
    elif number == 2:
        print("Tuesday")
    elif number == 3:
        print("Wednesday")
    elif number == 4:
        print("Thursday")
    elif number == 5:
        print("Friday")
    elif number == 6:
        print("Saturday")
    elif number ==7:
        print("Sunday")
    else:
        print("ERROR!!!")