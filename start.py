import cfg

# функция выбора параметров игры

def print_start_background():
    print(cfg.const.START_BACKGROUND)

# Функция выбора имени пользователя

def choose_username():
    username = input("Введите ваше имя: ")
    return username

# вывод приветственного сообщения
def print_hello_massage(username):
    print(f"{username}, Добро пожаловать в игру Snake! Или..")

# Выбор уровня сложности и приветствие

def choose_difficulty():
    print("""Выберите уровень сложности:
            1. Легкий
            2. Средний
            3. Сложный""")
    try:
        game_difficulty = input("Введите номер уровня: ")
        if game_difficulty in ["1", "2", "3"]:
            choosed_game_difficulty = game_difficulty
            return choosed_game_difficulty
        else:
            raise ValueError

    except ValueError:
        print("Некорректный ввод. Попробуйте еще раз.")
        return choose_difficulty()
        
