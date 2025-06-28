from levels import level_1, level_2, level_3, level_4

# перенаправление на уровень в зависимости от выбранного уровня сложности
def redirect_to_level(selected_difficulty):
    if selected_difficulty == "1":
        level_1.start_game_level1()
    elif selected_difficulty == "2":
        level_2.start_game_level2()
    elif selected_difficulty == "3":
        level_3.start_game_level3()
    elif selected_difficulty == "4":
        level_4.start_game_level4()

# перенаправление в случае проигрыша
def redirect_to_malware():
    pass

# перенаправление в случае выигрыша
def redirect_to_cake():
    pass