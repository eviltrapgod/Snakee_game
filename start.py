import cfg




start_msg = """
Добро пожаловать в игру Змейка, {username}!

"""
username = input("Введите ваше имя: ")
print(start_msg.format(username=username))


