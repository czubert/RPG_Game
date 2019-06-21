import random

from teams import Team
from character import *


class Engine:
    def __init__(self):
        self.teams_list = []
        self.team_order = random.randint(0, 1)  # randoms starting team
        self.rounds = 0

    def create_new_team(self, name):
        tmp_name = Team(name)
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
        self.rounds += 1
        char1 = self.choose_attacking_character()
        if char1.rounds_stunned:
            print(f'stunned, round: {self.rounds}')
            self.change_team_order()
            if char1.rounds_stunned > 0:
                char1.rounds_stunned -= 1
            return
        print(f'not stunned, round: {self.rounds}')
        if type(char1) is Support:
            char2 = self.choose_attacking_character()
            char1.act(char2)
            self.change_team_order()
        else:
            self.change_team_order()
            char2 = self.choose_attacking_character()
            char1.act(char2)


game = Engine()

team1 = game.create_new_team('Gangi Nowego Yorku')
team2 = game.create_new_team('Piraci z Karaibów')

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
for i in range(95):
    game.fight()
print(game.teams_list[0])
print(game.teams_list[1])
# print(game.choose_attacking_character())



#TODO:
'''
- Dobrze by było, żeby bohaterowie mogli levelować
I jakoś od tego uzależnić ich moce
- Możesz wymyślić jakiś inny rodzaj postaci i go dodać
- Brakuje mi nazw postaci, albo chociaż nazwy Teamu jak orientujesz "przed i po" rozgrywce
- A jak to będzie ogarnięte to chyba wypada się wziąć za strategię
Żeby nie było już losowo kto i losowo kogo - tylko nadać im jakieś priorytety
Że np. Najsilniejszy atakuje częściej, albo zawsze się atakuje najsłabszego
'''