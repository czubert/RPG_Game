import random

from teams import Team
from character import *


class Engine:
    def __init__(self):
        self.teams_list = []
        self.team_order = random.randint(0, 1)

    def create_new_team(self):
        tmp_name = Team()
        self.teams_list.append(tmp_name)
        return tmp_name

    def change_team_order(self):
        if self.team_order == 0:
            self.team_order = 1
        else:
            self.team_order = 0

    def choose_attacking_character(self):
        dream_team = self.teams_list[self.team_order]
        character_order = random.randint(0, len(dream_team) - 1)
        character = dream_team[character_order]
        return character

    def fight(self):
        char1 = self.choose_attacking_character()
        if type(char1) is Support:
            char2 = self.choose_attacking_character()
            char1.act(char2)
            self.change_team_order()
        else:
            self.change_team_order()
            char2 = self.choose_attacking_character()
            char1.act(char2)


game = Engine()

team1 = game.create_new_team()
team2 = game.create_new_team()

team1.add_character(Warrior(200))
team1.add_character(Sorceress())
team1.add_character(Warrior(200))
team1.add_character(Support(200))

team2.add_character(Warrior(200))
team2.add_character(Warrior(200))
team2.add_character(Warrior(200))
team2.add_character(Warrior(200))

# print(team1)
print(game.teams_list[0])
print(game.teams_list[1])
print()
for i in range(10):
    game.fight()
print(game.teams_list[0])
print(game.teams_list[1])
# print(game.choose_attacking_character())

