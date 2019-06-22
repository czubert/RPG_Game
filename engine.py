import random

from teams import Team
from character import *


class Engine:
    def __init__(self):
        """

        """
        self.teams_list = []
        self.team_order = random.randint(0, 1)  # randoms starting team
        self.rounds = 0

    def create_new_team(self, name):
        """

        :param name:
        :return:
        """
        tmp_name = Team(name)
        self.teams_list.append(tmp_name)
        return tmp_name

    def change_team_order(self):
        """

        """
        if self.team_order == 0:
            self.team_order = 1
        else:
            self.team_order = 0

    def choose_attacking_character(self):
        """

        :return:
        """
        dream_team = self.teams_list[self.team_order]
        character_order = random.randint(0, len(dream_team) - 1)
        character = dream_team[character_order]

        return character

    def fight(self):
        """

        :return:
        """
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
for i in range(195):
    game.fight()
print(game.teams_list[0])
print(game.teams_list[1])
# print(game.choose_attacking_character())


# TODO:
'''
- Dobrze by było, żeby bohaterowie mogli levelować, I jakoś od tego uzależnić ich moce
- Możesz wymyślić jakiś inny rodzaj postaci i go dodać
- A jak to będzie ogarnięte to chyba wypada się wziąć za strategię
Żeby nie było już losowo kto i losowo kogo - tylko nadać im jakieś priorytety
Że np. Najsilniejszy atakuje częściej, albo zawsze się atakuje najsłabszego
- formatowanie
- komentarze
- check if defeated to zło! nie używaj quit() w kodzie - to paskudne 😜
lepiej prowadzić walkę dopóki w obu drużynach jest jakaś postać. To w sumie aż się prosi o napisanie metody, 
która w odpowiedniej pętli wywołuje fight() a po tej pętli możesz wywołać jakieś podsumowanie
- sprawdzanie czy ktoś umarł: masz ten sam kawałek kodu w kilku miejscach. Zrób z tego metodę. To jest wspólna metoda 
dla wszystkich, którzy potrafią zabić, więc można ją wrzucić w jakieś jedno miejsce... 🙂 
A potem wywoływać np. w act
act jest lepsze niż np. attack, bo attack nie brzmi jakby miał sprawdzać czy zabił. Którego atakujacego to obchodzi? xD
- w heal(self, other) warto byłoby skorzystać z max(cośtam, cośtam_innego) zamiast z if/else
- a Check if poisoned totalnie nie ma szansy działać. 
1. poizonowanie powinno się odbywać tylko dla drużyny, która aktulanie wykonuje ruch, nie?
2. to charakter wie czy jest zapoizonowany czy nie. Trzeba go o to zapytać i jeśli jeśli jest to mu odjąć życie. 
Ile tego życia? Trzeba to gdzieś NA NIM przechowywać. Na razie zrób na sztywno jakąś wartosć, ale zaraz dodamy jakiś 
sprytny myk na to, żeby było wiadomo ile tych HP ma tracić. check_if_poisoned wydaje mi się metodą Team a nie Engine
'''
