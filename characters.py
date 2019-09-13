import random
from abc import ABC, abstractmethod
import names

import modifiers


class Character(ABC):
    lvl = 1  # initial character lvl
    exp = 0  # initial character experience
    exp_for_lvl = 500  # initial experience needed for next level
    exp_gained = 250  # initial experience per kill
    max_hp = None  # initial max hp, defined by specific character class
    max_mana = None  # initial max mana, defined by specific character class
    defence = None  # initial defence, defined by specific character class
    magic_immunity = None  # initial magic immunity, defined by specific character class

    def __str__(self) -> str:
        return f"Player: {self.name}, Level: {self.lvl}, Exp: {self.exp}/{self.exp_for_lvl}, " \
               f"Max HP: {self.max_hp}, Current HP: {self.current_hp}"

    def __init__(self, mana_regen, hp_regen, mana_regen_lvl_up, hp_regen_lvl_up) -> None:
        self.name = names.get_first_name()
        self.current_hp = self.max_hp
        self.current_mana = self.max_mana
        self.mana_regen = mana_regen
        self.hp_regen = hp_regen
        self.mana_regen_lvl_up = mana_regen_lvl_up
        self.hp_regen_lvl_up = hp_regen_lvl_up
        self.team = None
        self.modifier_list = []
        self.next_move = self.act

    @abstractmethod
    def act(self, other) -> None:
        """
        Uses action of character
        """
        pass

    @staticmethod
    def remove_if_dead(other: "opponent character object") -> bool:
        """
        Checks if attacked opponent is dead after attack on him, if yes delete it from the team
        :param other: opponent object
        """
        if other.current_hp < 0:  # checks if attack killed opponent
            other.team.team.remove(other)  # deletes dead character from its team
            return True
        else:
            return False

    def find_weakest_character(self) -> object:   # WHAT hints about return doesn't work
        """
        Finds weakest character from team
        :return: character object
        """
        return min(self.team.opponent_team, key=lambda x: x.current_hp)

    def regenerate(self) -> None:
        self._regenerate_hp()
        self._regenerate_mana()

    def _regenerate_hp(self) -> None:
        self.current_hp = min(self.max_hp, self.current_hp + self.hp_regen * self.max_hp)  # hp regeneration

    def _regenerate_mana(self) -> None:
        self.current_mana = min(self.max_mana, self.current_mana + self.mana_regen *
                                self.max_mana)  # hp regeneration# mana regeneration

    # def get_exp(self) -> None:
    #     self.exp += self.exp_gained
    #
    #     if self.exp > self.exp_for_lvl:
    #         self.lvl_up()

    def get_exp(self, other) -> None:
        """
        Gives exp to character after killing opponent, based on fighters strength.
        :param other: character object
        :return: None
        """
        self.check_str_and_give_exp(other)
        self.check_if_lvl_up()

    def check_if_lvl_up(self) -> None:
        """
        Checks if hero collected experience to gain next level
        :return: None
        """
        if self.exp > self.exp_for_lvl:
            self.lvl_up()

    def check_str_and_give_exp(self, other) -> None:
        """
        Checks if opponent is stronger/weaker or equally strong and give exp depending on it
        :param other: character object
        :return: None
        """
        exp_gained = 250 + 50 * (self.lvl - 1)

        for i in range(10000):
            self.check_if_lvl_up()
            if other.lvl == i:
                self.exp += exp_gained * 1.5 * (i ** 2) + 10000
                return


        if self.lvl > other.lvl:
            self.exp += exp_gained * 0.1
        elif self.lvl < other.lvl:
            self.exp += exp_gained * 0.5

    def lvl_up(self) -> None:
        self.lvl += 1
        self.exp_for_lvl += 1250 * self.lvl * 2
        self.max_hp += 50 * self.lvl
        self.regeneration_upgr_after_lvl_up(self.mana_regen_lvl_up, self.hp_regen_lvl_up)
        self.regenerate()

    def regeneration_upgr_after_lvl_up(self, mana_regen_lvl_up: int, hp_regen_lvl_up: int) -> None:
        self.mana_regen += mana_regen_lvl_up * self.lvl
        self.hp_regen += hp_regen_lvl_up * self.lvl

    def do_nothing(self, other) -> None:
        pass


class MagicType(Character, ABC):
    defence = 0.3
    magic_immunity = 0.65
    max_mana = 450

    def __init__(self) -> None:
        Character.__init__(self, hp_regen=0.01, hp_regen_lvl_up=0.0025, mana_regen=0.02, mana_regen_lvl_up=0.005)


class CarryType(Character, ABC):
    defence = 0.6
    magic_immunity = 0.25
    max_mana = 200

    def __init__(self) -> None:
        Character.__init__(self, hp_regen=0.02, hp_regen_lvl_up=0.005, mana_regen=0.01, mana_regen_lvl_up=0.0025)


class Warrior(CarryType):
    max_hp = 1300
    spell_mana_cost = 200
    physical_dmg = 200 + random.randint(0, 100)
    spell_dmg = random.randint(0, 200)

    def __init__(self) -> None:
        """
        Creates warrior character object
        """
        CarryType.__init__(self)

    def act(self, other: Character) -> None:
        self.attack(other)

        if self.remove_if_dead(other):
            self.get_exp(other)

    def attack(self, other: Character) -> None:
        """
        Skill of character, deals damage to opponent
        :param other: opponent character object
        """
        dmg_by_lvl = 1 + self.lvl * 0.1
        other.current_hp -= int((self.physical_dmg * dmg_by_lvl) * (1 - other.defence))


class Sorceress(MagicType):
    max_hp = 900
    spell_mana_cost = 35
    physical_dmg = random.randint(50, 100)
    spell_dmg = 50 + random.randint(0, 60)

    def __init__(self) -> None:
        """
        Creates sorceress character object
        """
        MagicType.__init__(self)

    def act(self, other: Character) -> None:
        if self.current_mana >= self.spell_mana_cost:
            self.stun(other)
        else:
            self.attack(other)

        if self.remove_if_dead(other):
            self.get_exp(other)

    def stun(self, other: Character) -> None:
        """
        Skill of character, stuns opponent
        :param other: opponent character object
        """
        stun = modifiers.Stun(self, other, 2)
        other.modifier_list.append(stun)
        other.current_hp -= int(self.spell_dmg * (1 - other.magic_immunity))

    def attack(self, other: Character) -> None:
        """
        Skill of character, deals damage to opponent
        :param other: opponent character object
        """
        other.current_hp -= int((self.physical_dmg * (1 + self.lvl * 0.1)) * (1 - other.defence))


class Support(MagicType):
    """
    Creates support character object
    """
    max_hp = 800
    spell_mana_cost = 95
    physical_dmg = random.randint(50, 70)
    healing_power = 100 + random.randint(40, 100)

    def __init__(self) -> None:
        MagicType.__init__(self)

    def act(self, other: Character) -> None:
        if self.current_mana >= self.spell_mana_cost:
            self.heal(other)
            if other.max_hp == other.current_hp:
                self.get_exp(other)
        else:
            self.attack(other)
            if self.remove_if_dead(other):
                self.get_exp(other)

    def heal(self, other: Character) -> None:
        """
        Heals character from own team - healing_power tells how much it heals
        :param other: character object, from own team
        """
        other.current_hp = min(other.current_hp + self.healing_power, other.max_hp)
        self.current_mana -= self.spell_mana_cost

    def find_weakest_character(self) -> Character:
        """
        Finds weakest character from team
        :return: character object
        """
        if self.current_mana >= self.spell_mana_cost:
            return min(self.team.team, key=lambda x: x.current_hp)
        else:
            return min(self.team.opponent_team, key=lambda x: x.current_hp)

    def attack(self, other: Character) -> None:
        """
        Skill of character, deals damage to opponent
        :param other: opponent character object
        """
        other.current_hp -= int(self.physical_dmg * (1 + self.lvl * 0.1))


class Voodoo(MagicType):
    max_hp = 1000
    spell_mana_cost = 55
    physical_dmg = 50
    spell_dmg = 75 + random.randint(0, 30)

    def __init__(self) -> None:
        MagicType.__init__(self)

    def act(self, other: Character) -> None:
        if self.current_mana >= self.spell_mana_cost:
            self.poison(other)
        else:
            self.attack(other)

        self.remove_if_dead(other)

    def poison(self, other: Character) -> None:
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

    def attack(self, other: Character) -> None:
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
