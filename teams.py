import random
import math

import characters


class Team:
    def __init__(self, name):
        self.name = name
        self.team = []
        self.opponent_team = None
        self.generator_field = None

    def __str__(self):
        return ' \n'.join([element.__str__() for element in self.team])

    def add_character(self, hero):
        """
        Adds character to a team and links character with it's team
        :param hero: Character object
        """
        self.team.append(hero)
        hero.team = self

    def team_generator(self, number):
        types_of_characters = [characters.Sorceress, characters.Warrior, characters.Support, characters.Voodoo]
        [self.add_character(random.choice(types_of_characters)()) for _ in range(number)]

    def __getitem__(self, item):
        return self.team.__getitem__(item)

    def __len__(self):
        return len(self.team)

    def team_act(self, char):
        """
        Randoms hero from team, checks if it has modificators on himself (if yes act), checks if randomed char is support
        if yes, then looks for weakest hero to heal him, if no, looks for weakest opponent to attack,
        regenerates mana and hp at the end of the round, gives exp to attacker
        :return:
        """

        # checks if choosen character has modifiers on him, if yes they are activated
        for modi in char.modifier_list:
            modi.act()

        if char.current_hp < 0:
            return

        if type(char) is characters.Support:
            target = self.find_weakest_character(self.team)
        else:
            target = self.find_weakest_character(self.opponent_team)

        char.act(target)

        char.get_exp()

    def find_attacking_character(self):
        # return random.choice(self.team)
        for char in self.team:
            yield char
        yield None

    def find_strongest_character(self):
        '''
        finds strongest character from team
        :return: character object
        '''
        pass

    def find_weakest_character(self, target_team):
        """
        Finds weakest character from team
        :return: character obcject
        """
        lowest_hp = math.inf
        weakest_character = None
        for character in target_team:
            if character.current_hp < lowest_hp:
                lowest_hp = character.current_hp
                weakest_character = character
        return weakest_character

    def after_round_regenerate_mana_and_hp(self):
