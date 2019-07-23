import random
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

    def team_generator(self, number):
        types_of_characters = [characters.Sorceress, characters.Warrior, characters.Support, characters.Voodoo]
        # chosen_char = random.choice(types_of_characters)
        [self.add_character(random.choice(types_of_characters)()) for _ in range(number)]

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
