# Перевірка паролю:
# Завдання: Напишіть програму, яка встановлює початковий пароль і перевіряє, 
# чи введений користувачем пароль співпадає з ним. 
# Якщо пароль дорівнює "password123", виведіть повідомлення "Ви увійшли в систему". 
# В іншому випадку виведіть повідомлення "Неправильний пароль".

passwords = ["gegfdgf", "gdfgeg54gfd", "fgdgf555", "password123", "gdfgdfe524"]

user_1 = {
    "name": "Mike",
    "password": "password123"
}

for password in passwords:
    if user_1["password"] != password:
        print(f"Sorry, {user_1["name"]}, you entered an incorrect password!")
        print("Please, try again!")
    else:
        print("You are logged in! Welcome to the club!!!")
        break