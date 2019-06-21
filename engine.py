import random

from teams import Team
from character import *


class Engine:
    def __init__(self):
        self.teams_list = []

    def create_new_team(self):
        tmp_name = Team()
        self.teams_list.append(tmp_name)
        return tmp_name

    def choose_fighter(self):
        order = random.randint(0, 1)
        fighter = self.teams_list[order]
        return fighter


game = Engine()

team1 = game.create_new_team()
team2 = game.create_new_team()

team1.add_character(Warrior(200))
team1.add_character(Sorceress())
team1.add_character(Support(200))
team1.add_character(Support(200))

team2.add_character(Warrior(200))
team2.add_character(Warrior(200))
team2.add_character(Warrior(200))
team2.add_character(Warrior(200))

# print(team1)
# print(game.teams_list[0])
# print(game.teams_list[1])
print(game.choose_fighter())