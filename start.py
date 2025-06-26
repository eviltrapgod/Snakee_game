import cfg

# функция выбора не постоянных параметров и приветствие
def choose_game_settings():
    print(cfg.START_BACKGROUND)
    # Функция выбора имени пользователя
    def choose_username():
        username = input("Введите ваше имя: ")
        start_msg = f"{username}, Добро пожаловать в игру Snake! Или.."
        return start_msg
    # Запись стартового сообщения в переменную
    start_msg = choose_username()

    # Выбор уровня сложности и приветствие
    def choose_level(start_msg):
        print(start_msg)
        print("""Выберите уровень сложности:
              1. Легкий
              2. Средний
              3. Сложный""")
        try:
            game_level = input("Введите номер уровня: ")
            if game_level not in ["1", "2", "3"]:
                raise ValueError
            else:
                return choose_level
        except ValueError:
            print("Некорректный ввод. Попробуйте еще раз.")
            return choose_level(start_msg)
        return game_level
    # запись в переменную выбранный уровень сложности
    game_level = choose_level(start_msg)

