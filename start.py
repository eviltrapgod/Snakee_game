import cfg, main

def start_game():
    print(cfg.START_BACKGROUND)

    def choose_username(start_msg):
        username = input("Введите ваше имя: ")
        start_msg = f"Добро пожаловать в игру Змейка, {username}!"
        return start_msg

    choose_username()


    def choose_level(start_msg):
        print(start_msg)
        print("""Выберите уровень сложности:
              1. Легкий
              2. Средний
              3. Сложный""")

        game_level = input("Введите номер уровня: ")
        return game_level
