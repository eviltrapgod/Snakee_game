import start, redirect, check_agreement
import sys
# вызов функциональной части программы
def main():
    # попытка выполнения программы 
    try:
        if not check_agreement.check_status():
            sys.exit()
        else:
            # вывод стартового экрана
            start.print_start_background()
            # выбор имени пользователя
            username = start.choose_username()
            # вывод приветственного сообщения
            start.print_hello_message(username)
            # выбор уровня сложности
            game_difficulty = start.choose_difficulty()
            # перенаправление в игру с выбранным уровнем сложности
            redirect.redirect_to_level(game_difficulty)
    # обработка ошибок
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        print("Пожалуйста, сообщите нам о ней на Github.")


# вход в программу
if __name__ == "__main__":
    main()