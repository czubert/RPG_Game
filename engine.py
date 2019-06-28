import random
import time

from teams import Team
from characters import *


class Engine:
    def __init__(self):
        self.teams_list = []
        self.team_order = random.randint(0, 1)  # randoms starting team
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

    def change_team_order(self):
        """
        Change attacking team to another one
        """
        if self.team_order == 0:
            self.team_order = 1
        else:
            self.team_order = 0

    def choose_attacking_character(self):
        """
        Randomly take team which will attack first, and then randomly choose character who will attack first
        :return: character object
        """
        dream_team = self.teams_list[self.team_order]  # randomly takes team from teams list
        character_order = random.randint(0, len(dream_team) - 1)  # randoms which character to take from team
        character = dream_team[character_order]  # takes character

        return character

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
        # # working version
        # while all(game.teams_list):
        #     self.rounds += 1  # counts the rounds
        #     char1 = self.choose_attacking_character()
        #
        #     for modi in char1.modifier_list:
        #         modi.act()
        #
        #     char1.get_exp()
        #     if type(char1) is Support:  # checks if active character is a support if yes he cast spell on random
        #         # character from its team
        #         char2 = self.choose_attacking_character()
        #         char1.next_move(char2)
        #         self.change_team_order()
        #     else:  # use act typical for its character on the random opponent character
        #         self.change_team_order()
        #         char2 = self.choose_attacking_character()
        #         char1.next_move(char2)

        while all(game.teams_list):
            self.rounds += 1  # counts the rounds
            char1 = self.choose_attacking_character()

            for modi in char1.modifier_list:
                modi.act()

            char1.get_exp()
            if type(char1) is Support:  # checks if active character is a support if yes he cast spell on random
                # character from its team
                char2 = self.choose_attacking_character()
                char1.next_move(Team.find_weakest_opponent(char2.team))
                self.change_team_order()
            else:  # use act typical for its character on the random opponent character
                self.change_team_order()
                char2 = self.choose_attacking_character()
                char1.next_move(Team.find_weakest_opponent(char2.team))

    def battle_summary(self):
        winning_team = list(filter(bool, self.teams_list))[0]

        return f"Team:{winning_team.name} \n Battle took: {self.rounds} rounds, {self.program_execution_time} s"


starting_time = time.time()
game = Engine()

team1 = game.create_new_team('Gangi Nowego Yorku')
team2 = game.create_new_team('Piraci z Karaibów')

time_after_teams_creation = time.time()

team1.team_generator(1000)
team2.team_generator(1000)

time_after_team_creation = time.time()

game.run_game()

print(f"Time of teams creation: {starting_time - time_after_teams_creation}, time of team members: "
      f"{time_after_team_creation - time_after_teams_creation}, general time: {time.time() - starting_time}")
