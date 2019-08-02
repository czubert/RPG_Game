import random
import math

import characters


class Team:
    def __init__(self, name):
        self.name = name
        self.team = []
        self.opponent_team = None

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

    def choose_char_and_act(self):
        """
        Randoms hero from team, checks if it has modificators on himself (if yes act), checks if randomed char is support
        if yes, then looks for weakest hero to heal him, if no, looks for weakest opponent to attack,
        regenerates mana and hp at the end of the round, gives exp to attacker
        :return:
        """
        char = next(self.find_attacking_character())

        # checks if choosen character has modifiers on him, if yes they are activated
        for modi in char.modifier_list:
            modi.act()

        if type(char) is characters.Support:
            target = self.find_weakest_character(self.team)
        else:
            target = self.find_weakest_character(self.opponent_team)

        char.act(target)

        self.regenerate_hp(char)
        self.regenerate_mana(char)
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

    @staticmethod
    def regenerate_hp(char):
        # # TODO: regeneration after each round for everyone not only for a hero that attacks
        if char.current_hp + 0.01 * char.current_hp >= char.max_hp:
            char.current_hp = char.max_hp
        else:
            char.current_hp = char.current_hp + 0.02 * char.current_hp  # hp regeneration

    @staticmethod
    def regenerate_mana(char):
        # # TODO: regeneration after each round for everyone not only for a hero that attacks
        if char.current_mana + 0.01 * char.current_mana >= char.max_mana:
            char.current_mana = char.max_mana
        else:
            char.current_hp = char.current_mana + 0.02 * char.current_mana  # hp regeneration
