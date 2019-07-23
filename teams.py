import random
import names
import math

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

    def hero_generator(self, types_of_character):
        '''
        generates particular hero
        :return:
        '''
        chosen_char = types_of_characters[random.randint(0, len(types_of_characters) - 1)]
        if chosen_char is characters.Support:
            return chosen_char(50, 150, names.get_first_name())  # dmg dealt, spell value, name sorcerress
        elif chosen_char is characters.Sorceress:
            return chosen_char(50, 100, names.get_first_name())  # dmg dealt, spell value, name sorcerress
        elif chosen_char is characters.Voodoo:
            return chosen_char(50, 75, names.get_first_name())  # dmg dealt, spell value, name sorcerress
        else:
            return chosen_char(200, names.get_first_name())  # dmg dealt, name others

    def team_generator(self, number):
        types_of_characters = [characters.Sorceress, characters.Warrior, characters.Support, characters.Voodoo]
        [self.add_character(self.hero_generator(types_of_characters)) for _ in range(number)]

    def __getitem__(self, item):
        return self.team.__getitem__(item)

    def __len__(self):
        return len(self.team)

    def find_strongest_character(self):
        '''
        finds strongest character from team
        :return: character object
        '''
        pass

    def find_weakest_character(self):
        '''
        Finds weakest character from team
        :return: character obcject
        '''
        lowest_hp = math.inf
        weakest_character = None
        for character in self.team:
            if character.current_hp < lowest_hp or lowest_hp == 0:
                lowest_hp = character.current_hp
                weakest_character = character
        return weakest_character
