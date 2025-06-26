import levels

def redirect_to_level(selected_difficulty):
    if selected_difficulty == "1":
        levels.start_game_level1()
    elif selected_difficulty == "2":
        levels.start_game_level2()
    elif selected_difficulty == "3":
        levels.start_game_level3()
