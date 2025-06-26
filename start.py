import cfg

# функция выбора не постоянных параметров и приветствие
def start_game():
    print(cfg.START_BACKGROUND)
    # Функция выбора имени пользователя
    def choose_username():
        username = input("Введите ваше имя: ")
        start_msg = f"Добро пожаловать в игру Snake, {username}!"
        return start_msg
    
    start_msg = choose_username()

    # Выбор уровня сложности и приветствие
    def choose_level(start_msg):
        print(start_msg)
        print("""Выберите уровень сложности:
              1. Легкий
              2. Средний
              3. Сложный""")
        game_level = input("Введите номер уровня: ")
        return game_level
    # запись в переменную выбранный уровень сложности
    game_level = choose_level(start_msg)

