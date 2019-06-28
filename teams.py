import random
import names

import characters


class Team:
    def __init__(self, name):
        self.name = name
        self.team = []

    def __str__(self):
        return ' \n'.join([element.__str__() for element in self.team])

    def add_character(self, hero):
        '''
        Adds character to a team and links character with it's team
        :param hero: Character object
        '''
        self.team.append(hero)
        hero.team = self

    def hero_generator(self):
        '''
        generates particular hero
        :return:
        '''
        types_of_characters = [characters.Sorceress, characters.Warrior, characters.Support, characters.Voodoo]
        chosen_char = types_of_characters[random.randint(0, len(types_of_characters) - 1)]
        if chosen_char in [characters.Sorceress, characters.Voodoo]:
            return chosen_char(50, names.get_first_name())  # dmg dealt, name sorcerress
        else:
            return chosen_char(200, names.get_first_name())  # dmg dealt, name others

    def team_generator(self, number):
        [self.add_character(self.hero_generator()) for _ in range(number)]

    def __getitem__(self, item):
        return self.team.__getitem__(item)

    def __len__(self):
        return len(self.team)

    def find_stronges_warrior(self):
        pass

    def find_weakest_opponent(self):
        lowest_hp = 0
        weakest_character = None
        for character in self.team:
            if character.current_hp < lowest_hp or lowest_hp == 0:
                lowest_hp = character.current_hp
                weakest_character = character
        return weakest_character
