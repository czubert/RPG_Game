import time
import os
import datetime

import engine

start_time = time.time()


x = datetime.datetime.now()

num_of_games = 4

folder_name = f'{x.year}-{x.month}-{x.day}-{x.hour}{x.minute}-game'
newpath = f'results/{folder_name}'

if not os.path.exists(newpath):
    os.makedirs(newpath)

for i in range(1, 3):
    team1_size = 10 ** i
    team2_size = 10 ** i

    game_name = f'{team1_size}x{team2_size}-{num_of_games}games'

    for num in range(num_of_games):
        game = engine.Engine(team1_size, team2_size)
        game.run_game()
        with open(f"results/{folder_name}/{game_name}.csv", "a") as f:
            f.write(f"{team1_size},{team2_size},{game.battle_summary()}\n")

program_execution_time = round(time.time() - start_time, 4)
print(f'\nBuild in: {program_execution_time} s | {round(program_execution_time / 60, 4)} min | '
      f'{round((program_execution_time / 60) / 60, 4)} h')
