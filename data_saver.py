import time
import os
import datetime

import engine


class DataSaver:
    def __init__(self, num_of_games=10):
        # # defines number of games and the size of a team (the size is 10 to the power of team_size) and it defines how
        # many different matches will be played like: 2 - 10x10 and 100x100
        self.num_of_games = num_of_games

    #     self.team_size = team_size

    @staticmethod
    def create_path():
        # # creates folder for results if it doesn't exist, if it exists then it is just setting it up
        new_path = 'results'
        if not os.path.exists(new_path):
            os.makedirs(new_path)

    def file_name(self):
        # # defines saved file name
        x = datetime.datetime.now()
        game_name = f'{x.year}-{x.month}-{x.day}-{x.hour}{x.minute:03} - {self.num_of_games} games'
        return game_name

    def save_data(self, team1_size, team2_size, round_number, game):
        with open(f"results/{self.file_name()}.csv", "a") as f:
            f.write(f"{int(round_number)}, {int(team1_size)},{int(team2_size)},{game.battle_summary()}\n")

    def run(self, team1_size, team2_size):
        start_time = time.time()

        round_number = 0

        for num in range(self.num_of_games):
            game = engine.Engine(team1_size, team2_size)
            game.run_game()

            round_number += 1

            self.save_data(team1_size, team2_size, round_number, game)

        program_execution_time = round(time.time() - start_time, 4)

        print(f'\nBuild in: {program_execution_time} s | {round(program_execution_time / 60, 4)} min | '
              f'{round((program_execution_time / 60) / 60, 4)} h')


if __name__ == '__main__':
    team1_characters = 100
    team2_characters = 100
    num_of_battles = 1
    for i in range(1, 2):
        data = DataSaver(num_of_battles* 10**i)
        data.run(team1_characters, team2_characters)
