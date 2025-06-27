import start, redirect, check_agreement
import sys
# вызов функциональной части программы
def main(username, game_difficulty):
    # проверка статуса соглашения с условиями пользования
    if check_agreement.check_agreement_status() == False:
        sys.exit()
    elif check_agreement.check_agreement_status() == True:
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

# вход в программу
if __name__ == "__main__":
    main("username", "game_difficulty")