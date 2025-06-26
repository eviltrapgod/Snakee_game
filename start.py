import cfg

def start_game():
    username = input("Введите ваше имя: ")
    print(cfg.start_msg.format(username=username))


