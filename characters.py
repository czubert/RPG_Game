import random
from abc import ABC, abstractmethod

import modifiers


class MagicType:
    def __init__(self):
        self.defence = 0.3
        self.max_mana = 450
        self.current_mana = self.max_mana


class CarryType:
    def __init__(self):
        self.defence = 0.6
        self.max_mana = 200
        self.current_mana = self.max_mana


class Character(ABC):
    def __init__(self, max_hp, name):
        self.name = name
        self.lvl = 1
        self.exp_for_lvl = 500  # experience needed to lvl_up
        self.exp = 0
        self.max_hp = max_hp
        self.current_hp = self.max_hp
        self.team = None
        self.modifier_list = []
        self.next_move = self.act

    def __str__(self):
        return f"Player: {self.name}, Level: {self.lvl}, Exp: {self.exp}/{self.exp_for_lvl}, " \
            f"Max HP: {self.max_hp}, Current HP: {self.current_hp}, Rounds to get ready:"

    @abstractmethod
    def act(self, other):
        """
        Uses action of character
        """
        pass

    @staticmethod
    def remove_if_dead(other):
        """
        Checks if attacked opponent is dead after attack on him, if yes delete it from the team
        :param other: opponent object
        """
        if other.current_hp < 0:  # checks if attack killed opponent
            other.team.team.remove(other)  # deletes dead character from its team

    def get_exp(self):
        self.exp += 250

        if self.exp > self.exp_for_lvl:
            self.lvl_up()

    def lvl_up(self):
        self.lvl += 1
        self.exp_for_lvl = 1250 * self.lvl
        self.max_hp += 300 * self.lvl

    def do_nothing(self, other):
        pass


class Warrior(Character, CarryType):
    def __init__(self, attack_power, name):
        """
        Creates warrior character object
        :param attack_power: int, damage that character deals
        :param name: str, name of character
        """
        Character.__init__(self, 1300, name)
        CarryType.__init__(self)
        self.attack_power = attack_power + random.randint(0, 100)

    def act(self, other):
        self.attack(other)
        self.remove_if_dead(other)

    def attack(self, other):
        """
        Skill of character, deals damage to opponent
        :param other: opponent character object
        """
        other.current_hp -= int(self.attack_power * (1 + self.lvl * 0.1))


class Sorceress(Character, MagicType):
    def __init__(self, attack_power, name):
        """
        Creates sorceress character object
        :param name: str, name of character
        """
        Character.__init__(self, 900, name)
        MagicType.__init__(self)
        self.attack_power = attack_power + random.randint(0, 80)

    def act(self, other):
        self.stun(other)
        self.attack(other)
        self.remove_if_dead(other)

    def stun(self, other):
        """
        Skill of character, stuns opponent
        :param other: opponent character object
        """
        stun = modifiers.Stun(self, other, 2)
        other.modifier_list.append(stun)

    def attack(self, other):
        """
        Skill of character, deals damage to opponent
        :param other: opponent character object
        """
        other.current_hp -= int(self.attack_power * (1 + self.lvl * 0.1))


class Support(Character, MagicType):
    """
    Creates support character object
    """

    def __init__(self, healing_power, name):
        """
        :param healing_power: int, hp that character regenerates
        :param name: str, name of character
        """
        Character.__init__(self, 800, name)
        MagicType.__init__(self)
        self.healing_power = healing_power

    def act(self, other):
        self.heal(other)

    def heal(self, other):
        """
        Heals character from own team - healing_power tells how much it heals
        :param other: character object, from own team
        """
        min(other.current_hp + self.healing_power, other.max_hp)


class Voodoo(Character, MagicType):
    def __init__(self, poison_nova, name):
        MagicType.__init__(self)
        Character.__init__(self, 1000, name)
        self.poison_nova = poison_nova

    def act(self, other):
        self.poison(other)
        self.remove_if_dead(other)

    def poison(self, other):
        for modifier in other.modifier_list:
            if not isinstance(modifier, modifiers.Poison):
                continue
            elif isinstance(modifier, modifiers.Poison):
                if self.lvl > 10:
                    modifier.duration += int(1 + self.lvl / 2)
                elif self.lvl > 5:
                    modifier.duration += int(1 + self.lvl / 3)
                else:
                    modifier.duration += 1
            else:
                poison = modifiers.Poison(self, other, 3, self.poison_nova)
                other.modifier_list.append(poison)

    # def poison(self, other):
    #     if self.poison not in other.modifier_list:
    #         poison = modifiers.Poison(self, other, 3, self.poison_nova)
    #         other.modifier_list.append(poison)
    #     else:
    #         for modifier in other.modifier_list:
    #             if not isinstance(modifier, modifiers.Poison):
    #                 continue
    #             elif isinstance(modifier, modifiers.Poison):
    #                 if self.lvl > 10:
    #                     modifier.duration += int(1 + self.lvl / 2)
    #                 elif self.lvl > 5:
    #                     modifier.duration += int(1 + self.lvl / 3)
    #                 else:
    #                     modifier.duration += 1

    # def poison(self, other):
    #     if modifiers.Poison not in other.modifier_list:
    #         poison = modifiers.Poison(self, other, 3, self.poison_nova)
    #         other.modifier_list.append(poison)
    #     else:
    #         for modifier in other.modifier_list:
    #             if isinstance(modifier, modifiers.Poison):
    #                 if self.lvl > 10:
    #                     modifier.duration += int(1 + self.lvl / 2)
    #                 elif self.lvl > 5:
    #                     modifier.duration += int(1 + self.lvl / 3)
    #                 else:
    #                     modifier.duration += 1

# if __name__ == '__main__':
#     war1 = Warrior(300)
#     sorc1 = Sorceress()
#     supp1 = Support(100)
#     # vodo1 = Voodoo(50)
#
#     war1.act(supp1)
#     supp1.act(supp1)
#     war1.act(supp1)
#
#     print(war1.current_hp)
#     print(sorc1.current_hp)
#     print(supp1.current_hp)
#
#     print(war1)
