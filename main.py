import start, redirect_to_level

# вызов функциональной части программы
def main():
    start.print_start_background()
    username = start.choose_username()
    start.print_hello_message(username)
    game_difficulty = start.choose_difficulty()

# вход в программу
if __name__ == "__main__":
    main()