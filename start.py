import cfg
import os 
# функция выбора параметров игры

def print_start_background():
    print(cfg.const.START_BACKGROUND)

# Функция выбора имени пользователя
def choose_username():
    # Проверка на существование файла с именем пользователя
    if os.path.exists("data/username.txt"):
        # Чтение предыдущего имени пользователя
        with open("data/username.txt", "r") as f:
            previous_username = f.read().strip()
            # Предложение использовать предыдущее имя
        use_previous = input(f"Вы хотите использовать предыдущее имя '{previous_username}'? (да/нет): ")
        # Проверка ответа пользователя
        if use_previous.lower() in cfg.const.ANSW_YES_LIST:
            username = previous_username
        elif use_previous.lower() in cfg.const.ANSW_NO_LIST:
            username = input("Введите ваше новое имя: ")
            with open("data/username.txt", "w") as f:
                f.write(username)
            return username
        else:
            print("Некорректный ввод. Пожалуйста, ответьте 'да' или 'нет'.")
            return choose_username()
    # Если файла с именем пользователя нет
    else:
        username = input("Введите ваше имя: ")
        with open("data/username.txt", "w") as f:
            f.write(username)
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
