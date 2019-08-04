import random
import time

from teams import Team
from characters import *


class Engine:
    def __init__(self):
        self.teams_list = []
        # self.team_order = random.randint(0, 1)  # randoms starting team
        self.rounds = 0
        self.program_execution_time = 0

    def create_new_team(self, name):
        """
        Creates Team and sets it's name
        :param name: str
        :return: str, teams name
        """
        tmp_name = Team(name)
        self.teams_list.append(tmp_name)
        return tmp_name

    def run_game(self):
        start_time = time.time()
        self.fight()
        self.program_execution_time = time.time() - start_time
        print(self.battle_summary())

    def fight(self):
        """
        Takes character that is randomed to start fight, and attacks randomed character from opponents team
        If Character has skills working on your own team it also takes round.
        After attack/support it changes the team to another one.
        :return: Stops attack if chosen character is stunned
        """

        while all(game.teams_list):
            tmp_list = self.teams_list.copy()

            for team in tmp_list:
                team.generator_field = team.find_attacking_character()

            while tmp_list:
                for team in tmp_list:
                    char = next(team.generator_field)
                    if char is None:
                        tmp_list.remove(team)
                    else:
                        if team.opponent_team.team:
                            team.team_act(char)

            # on round end
            for team in self.teams_list:
                team.after_round_regenerate_mana_and_hp()

                self.rounds += 1  # counts the rounds

    def battle_summary(self):
        winning_team = list(filter(bool, self.teams_list))[0]

        return f"Team:{winning_team.name}\n Battle took: {self.rounds} rounds, {self.program_execution_time} s"


starting_time = time.time()
# # creates game object based on Engine class
game = Engine()

# # creates two opposite team objects and gives them names
team1 = game.create_new_team('Gangi Nowego Yorku')
team2 = game.create_new_team('Piraci z Karaibów')

time_after_teams_creation = time.time()

# # creates characters for both teams and adds them to the teams
team1.team_generator(500)
team2.team_generator(500)

# # now one team is known by the other one
team1.opponent_team = team2
team2.opponent_team = team1
print(f'team1:{len(team1.team)}, team1 opponents:{len(team1.opponent_team.team)}')

time_after_team_creation = time.time()

# # starts game
game.run_game()

print(f"Time of teams creation: {starting_time - time_after_teams_creation}, time of completing teams: "
      f"{time_after_team_creation - time_after_teams_creation}, general time: {time.time() - starting_time}")
