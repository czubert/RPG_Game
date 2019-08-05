import engine
import time
import os
import datetime

x = datetime.datetime.now()

num_of_games = 10

folder_name = f'{x.year}-{x.month}-{x.day}-{x.hour}{x.minute}-game'
newpath = f'results/{folder_name}'

if not os.path.exists(newpath):
    os.makedirs(newpath)

for i in range(1, 11):
    team1_size = i
    team2_size = i
    game_name = f'{team1_size}x{team2_size}-{num_of_games}games'

    # folder_name = f'game{team1_size}'
    # newpath = f'results/{folder_name}'
    #
    # if not os.path.exists(newpath):
    #     os.makedirs(newpath)

    for game in range(num_of_games):
        game = engine.Engine(team1_size, team2_size)
        game.run_game()
        with open(f"results/{folder_name}/{game_name}.csv", "a") as f:
            f.write(f"{team1_size},{team2_size},{game.battle_summary()}\n")

# name = f'{game_name}{game}'
