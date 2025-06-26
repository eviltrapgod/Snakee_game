import levels
import start

if start.game_difficulty == "1":
    levels.start_game_level1()
elif start.game_difficulty == "2":
    levels.start_game_level2()
elif start.game_difficulty == "3":
    levels.start_game_level3()