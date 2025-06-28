import cfg
import os 
# функция выбора параметров игры

def print_start_background():
    print(cfg.const.START_BACKGROUND)


# Функция выбора имени пользователя
def choose_username():
    if os.path.exists("username.txt"):
        with open("username.txt", "r") as f:
            previous_username = f.read().strip()
        use_previous = input(f"Вы хотите использовать предыдущее имя '{previous_username}'? (да/нет): ")
        if use_previous.lower() in cfg.const.ANSW_YES_LIST:
            username = previous_username
        else:
            username = input("Введите ваше новое имя: ")
            f = open("username.txt", "w")
            f.write(username)
            f.close()
            return username
    else:
        username = input("Введите ваше имя: ")
        f = open("username.txt", "w")
        f.write(username)
        f.close()
    return username

# Вывод приветственного сообщения
def print_hello_message(username):
    print(f"{username}, Добро пожаловать в игру Snake!")

# Выбор уровня сложности 

def choose_difficulty():
    print("""Выберите уровень сложности:
            1. Легкий
            2. Средний
            3. Сложный
            4. Очень сложный
            """)
    try:
        selected_difficulty = input("Введите номер уровня сложности: ")
        if selected_difficulty in ["1", "2", "3", "4"]:
            return selected_difficulty
        else:
            raise ValueError
    except ValueError:
        print("Неверный номер уровня сложности. Попробуйте еще раз.")
        return choose_difficulty()
