import cfg, main

def start_game():
    print(cfg.START_BACKGROUND)

    def choose_username():
        global username
        username = input("Введите ваше имя: ")
        global start_msg
        start_msg = f"""
        Добро пожаловать в игру Змейка, {username}!
            """


    choose_username()





    def choose_level():
        pass
    print(start_msg)
    