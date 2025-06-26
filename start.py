import cfg

# функция выбора не постоянных параметров и приветствие

def print_start_background():
    print(cfg.START_BACKGROUND)

def choose_game_settings():
    # Функция выбора имени пользователя
    def choose_username():
        username = input("Введите ваше имя: ")
        start_msg = f"{username}, Добро пожаловать в игру Snake! Или.."
        return start_msg
    # Запись стартового сообщения в переменную
    start_msg = choose_username()    
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
    # запись в переменную выбранный уровень сложности
    choosed_game_difficulty = choose_difficulty()

