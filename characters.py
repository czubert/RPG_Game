import random
from abc import ABC, abstractmethod
import names
import math

import modifiers


class Character(ABC):
    def __init__(self, max_hp, max_mana, defence, magic_immunity, mana_regen, hp_regen, spell_mana_cost,
                 mana_regen_lvl_up, hp_regen_lvl_up, physical_dmg):
        self.name = names.get_first_name()
        self.lvl = 1
        self.exp_for_lvl = 500  # experience needed to lvl_up
        self.exp = 0
        self.max_hp = max_hp
        self.current_hp = self.max_hp
        self.max_mana = max_mana
        self.current_mana = self.max_mana
        self.defence = defence
        self.magic_immunity = magic_immunity
        self.mana_regen = mana_regen
        self.hp_regen = hp_regen
        self.spell_mana_cost = spell_mana_cost
        self.mana_regen_lvl_up = mana_regen_lvl_up
        self.hp_regen_lvl_up = hp_regen_lvl_up
        self.physical_dmg = physical_dmg

        self.team = None
        self.modifier_list = []
        self.next_move = self.act

    def __str__(self):
        return f"Player: {self.name}, Level: {self.lvl}, Exp: {self.exp}/{self.exp_for_lvl}, " \
            f"Max HP: {self.max_hp}, Current HP: {self.current_hp}"

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

    def find_weakest_character(self):
        """
        Finds weakest character from team
        :return: character obcject
        """
        lowest_hp = math.inf
        weakest_character = None
        for character in self.team.opponent_team:
            if character.current_hp < lowest_hp:
                lowest_hp = character.current_hp
                weakest_character = character
        return weakest_character

    def regenerate(self):
        self.regenerate_hp()
        self.regenerate_mana()

    def regenerate_hp(self):
        if self.current_hp + self.hp_regen * self.current_hp >= self.max_hp:
            self.current_hp = self.max_hp
        else:
            self.current_hp = self.current_hp + self.hp_regen * self.max_hp  # hp regeneration

    def regenerate_mana(self):
        if self.current_mana + self.mana_regen * self.current_mana >= self.max_mana:
            self.current_mana = self.max_mana
        else:
            self.current_mana = self.current_mana + self.mana_regen * self.max_mana  # hp regeneration

    def get_exp(self):
        self.exp += 250

        if self.exp > self.exp_for_lvl:
            self.lvl_up()

    def lvl_up(self):
        self.lvl += 1
        self.exp_for_lvl = (1250 * self.lvl)
        self.max_hp += (50 * self.lvl)
        self.regeneration_upgr_after_lvl_up(self.mana_regen_lvl_up, self.hp_regen_lvl_up)
        self.regenerate()

    def regeneration_upgr_after_lvl_up(self, mana_regen_lvl_up, hp_regen_lvl_up):
        self.mana_regen += mana_regen_lvl_up * self.lvl
        self.hp_regen += hp_regen_lvl_up * self.lvl

    def do_nothing(self, other):
        pass


class MagicType(Character, ABC):
    def __init__(self, max_hp, physical_dmg, spell_mana_cost):
        Character.__init__(self, max_hp, max_mana=450, magic_immunity=0.65, defence=0.3, mana_regen=0.02, hp_regen=0.01,
                           mana_regen_lvl_up=0.005, hp_regen_lvl_up=0.0025, spell_mana_cost=spell_mana_cost,
                           physical_dmg=physical_dmg)


class CarryType(Character, ABC):
    def __init__(self, max_hp, physical_dmg, spell_mana_cost):
        Character.__init__(self, max_hp, max_mana=200, magic_immunity=0.25, defence=0.6, mana_regen=0.01, hp_regen=0.02,
                           mana_regen_lvl_up=0.0025, hp_regen_lvl_up=0.005, physical_dmg=physical_dmg,
                           spell_mana_cost=spell_mana_cost)


class Warrior(CarryType):
    def __init__(self):
        """
        Creates warrior character object
        """
        tmp_physical_dmg = 200 + random.randint(0, 100)
        self.spell_dmg = random.randint(0, 200)
        CarryType.__init__(self, max_hp=1300, physical_dmg=tmp_physical_dmg, spell_mana_cost=200)

    def act(self, other):
        self.attack(other)
        self.remove_if_dead(other)

    def attack(self, other):
        """
        Skill of character, deals damage to opponent
        :param other: opponent character object
        """
        other.current_hp -= int((self.physical_dmg * (1 + self.lvl * 0.1)) * (1 - other.defence))


class Sorceress(MagicType):
    def __init__(self):
        """
        Creates sorceress character object
        """
        tmp_physical_dmg = random.randint(50, 100)
        self.spell_dmg = 50 + random.randint(0, 60)
        MagicType.__init__(self, max_hp=900, physical_dmg=tmp_physical_dmg,
                           spell_mana_cost=35)

    def act(self, other):
        if self.current_mana >= self.spell_mana_cost:
            self.stun(other)
        else:
            self.attack(other)

        self.remove_if_dead(other)

    def stun(self, other):
        """
        Skill of character, stuns opponent
        :param other: opponent character object
        """
        stun = modifiers.Stun(self, other, 2)
        other.modifier_list.append(stun)
        other.current_hp -= int(self.spell_dmg * (1 - other.magic_immunity))

    def attack(self, other):
        """
        Skill of character, deals damage to opponent
        :param other: opponent character object
        """
        other.current_hp -= int((self.physical_dmg * (1 + self.lvl * 0.1)) * (1 - other.defence))


class Support(MagicType):
    """
    Creates support character object
    """

    def __init__(self):
        tmp_physical_dmg = random.randint(50, 100)
        self.healing_power = 100 + random.randint(40, 100)
        MagicType.__init__(self, max_hp=800, physical_dmg=tmp_physical_dmg, spell_mana_cost=55)

        # # debuggers:
        self.spell_counter = 0
        self.attack_counter = 0

    def act(self, other):
        if self.current_mana >= self.spell_mana_cost:
            self.heal(other)

        self.remove_if_dead(other)

    def heal(self, other):
        """
        Heals character from own team - healing_power tells how much it heals
        :param other: character object, from own team
        """
        other.current_hp = min(other.current_hp + self.healing_power, other.max_hp)
        self.current_mana -= self.spell_mana_cost
        self.spell_counter += 1

    def find_weakest_character(self):
        """
        Finds weakest character from team
        :return: character obcject
        """
        lowest_hp = math.inf
        weakest_character = None
        for character in self.team.team:
            if character.current_hp < lowest_hp:
                lowest_hp = character.current_hp
                weakest_character = character
        return weakest_character

    # TODO: Needs improvements in engine, otherwise it will hit his own teammate
    def attack(self, other):
        """
        Skill of character, deals damage to opponent
        :param other: opponent character object
        """
        other.current_hp -= int(self.physical_dmg * (1 + self.lvl * 0.1))
        self.attack_counter += 1


class Voodoo(MagicType):
    def __init__(self):
        self.spell_dmg = 75 + random.randint(0, 30)
        MagicType.__init__(self, max_hp=1000, physical_dmg=50, spell_mana_cost=55)

    def act(self, other):
        if self.current_mana >= self.spell_mana_cost:
            self.poison(other)
        else:
            self.attack(other)

        self.remove_if_dead(other)

    def poison(self, other):
        """
        Poison method checks if poison modifier is in the character list of modifiers.
        If yes then according to voodoo character lvl it extends duration
        If not then it adds poison modifier to the list of opponent modifiers
        :param other: opponent character object
        """
        if self.current_mana >= self.spell_mana_cost:
            poison_in_modifiers = False
            for modifier in other.modifier_list:
                if isinstance(modifier, modifiers.Poison):
                    poison_in_modifiers = True
                    if self.lvl > 10:
                        modifier.duration += int(1 + self.lvl / 4)
                    elif self.lvl > 5:
                        modifier.duration += int(1 + self.lvl / 5)
                    else:
                        modifier.duration += 1
            if not poison_in_modifiers:
                poison = modifiers.Poison(self, other, 3, self.spell_dmg)
                other.modifier_list.append(poison)

    def attack(self, other):
        """
        Skill of character, deals damage to opponent
        :param other: opponent character object
        """
        other.current_hp -= int(self.physical_dmg * (1 + self.lvl * 0.1))
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
