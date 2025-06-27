import cfg


# функция выбора параметров игры

def print_start_background():
    print(cfg.const.START_BACKGROUND)

# Функция выбора имени пользователя

def choose_username():
    username = input("Введите ваше имя: ")
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
