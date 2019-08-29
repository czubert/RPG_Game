import time
import os
import datetime

import engine

start_time = time.time()


x = datetime.datetime.now()

# # defines number of games and the size of a team (the size is 10 to the power of team_size) and it defines how
# many different matches will be played like: 2 - 10x10 and 100x100
num_of_games = 1000
team_size = 3

# # creates folder for results if it doesn't exist, if it exists then it is just setting it up
newpath = f'results'
if not os.path.exists(newpath):
    os.makedirs(newpath)

# # defines saved file name
if x.minute < 10:
    if_less_than_10min = 0  # for good order of the file names 1209 not 129 (for 12:09)
else:
    if_less_than_10min = ''
game_name = f'{x.year}-{x.month}-{x.day}-{x.hour}{if_less_than_10min}{x.minute} - {num_of_games} games'

# # sets the header of the files
# with open(f"results/{game_name}.csv", "a") as f:
#     f.write(f"Round number, Team 1 size,Team 2 size, Game rounds, Duration, Winning team")

for i in range(2, team_size):
    team1_size = 10 ** i
    team2_size = 10 ** i
    round_number = 0

    for num in range(num_of_games):
        game = engine.Engine(team1_size, team2_size)
        game.run_game()
        round_number += 1
        with open(f"results/{game_name}.csv", "a") as f:
            f.write(f"{round_number}, {team1_size},{team2_size},{game.battle_summary()}\n")

program_execution_time = round(time.time() - start_time, 4)
print(f'\nBuild in: {program_execution_time} s | {round(program_execution_time / 60, 4)} min | '
      f'{round((program_execution_time / 60) / 60, 4)} h')
