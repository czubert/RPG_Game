import random

from teams import Team
from character import *


class Engine:
    def __init__(self):
        self.teams_list = []
        self.team_order = random.randint(0, 1)  # randoms starting team
        self.rounds = 0

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
        self.fight()
        self.battle_summary()

    def fight(self):
        """
        Takes character that is randomed to start fight, and attacks randomed character from opponents team
        If Character has skills working on your own team it also takes round.
        After attack/support it changes the team to another one.
        :return: Stops attack if chosen character is stunned
        """
        while len(game.teams_list[0]) and len(game.teams_list[1]) != 0:
            self.rounds += 1  # counts the rounds
            char1 = self.choose_attacking_character()
            if char1.rounds_stunned:  # checks if randomed character is stunned, if yes it stops goes to next attack
                print(f'stunned, round: {self.rounds}')
                self.change_team_order()
                if char1.rounds_stunned > 0:
                    char1.rounds_stunned -= 1  # after round stunned characters has 1 round of stun less
                continue
            print(f'not stunned, round: {self.rounds}')

            if type(char1) is Support:  # checks if active character is a support if yes he cast spell on random
                # character from its team
                char2 = self.choose_attacking_character()
                char1.act(char2)
                self.change_team_order()
            else:  # use act typical for its character on the random opponent character
                self.change_team_order()
                char2 = self.choose_attacking_character()
                char1.act(char2)

    def battle_summary(self):
        for element in game.teams_list:
            return f"Team: {self.team.name} won the battle \n Survivors: {self.team}"



game = Engine()

team1 = game.create_new_team('Gangi Nowego Yorku')
team2 = game.create_new_team('Piraci z Karaibów')

team1.add_character(Warrior(200, 'Brajan'))
team1.add_character(Sorceress('Jessica'))
team1.add_character(Warrior(200, 'Ken'))
team1.add_character(Support(200, 'Majk'))

team2.add_character(Warrior(200, 'Jack'))
team2.add_character(Warrior(200, 'Sparrow'))
team2.add_character(Warrior(200, 'Czarna Perla'))
team2.add_character(Warrior(200, 'Holender'))

# print(team1)
print(game.teams_list[0])
print(game.teams_list[1])
print()
game.fight()
print(game.teams_list[0])
print(game.teams_list[1])
# print(game.choose_attacking_character())
