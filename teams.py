import random

import characters


class Team:
    def __init__(self, name: str) -> None:
        self.name = name
        self.team = []
        self.opponent_team = None
        self.generator = None
        self.number_of_survivors = len(self.team)

    def __str__(self) -> str:
        return ' \n'.join([element.__str__() for element in self.team])

    def add_character(self, hero) -> None:
        """
        Adds character to a team and links character with it's team
        :param hero: Character object
        """
        self.team.append(hero)
        hero.team = self

    def team_generator(self, number: int) -> None:
        types_of_characters = [characters.Sorceress, characters.Warrior, characters.Support, characters.Voodoo]
        [self.add_character(random.choice(types_of_characters)()) for _ in range(number)]

    def __getitem__(self, item: int):
        return self.team.__getitem__(item)

    def __len__(self) -> int:
        return len(self.team)

    @staticmethod
    def team_act(char) -> None:
        """
        Randoms hero from team, checks if it has modificators on himself (if yes act),
        checks if drawn char is support if yes, then looks for weakest hero to heal him,
        if no, looks for weakest opponent to attack, regenerates mana and hp at the end of the round,
        gives exp to attacker.
        :return:
        """

        # checks if chosen character has modifiers on him, if yes they are activated
        for modi in char.modifier_list:
            modi.act()

        if char.current_hp < 0:
            return

        target = char.find_weakest_character()

        char.next_move(target)

    # generator going through team list one by one, if it reaches the end it raise an error
    def find_attacking_character(self):
        for char in self.team:
            yield char
        yield None

    def find_strongest_character(self) -> None:
        """
        finds strongest character from team
        :return: character object
        """
        pass

    def after_round_regenerate_mana_and_hp(self) -> None:
        for char in self.team:
            char.regenerate()
