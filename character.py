import random
from abc import ABC, abstractmethod


class Character(ABC):
    def __init__(self, max_hp, name):
        self.name = name
        self.lvl = 1
        self.exp_for_lvl = 500  # experience needed to lvl_up
        self.exp = 0
        self.max_hp = max_hp
        self.current_hp = self.max_hp
        self.rounds_stunned = 0
        self.rounds_poisoned = 0
        self.team = None

    def __str__(self):
        return f"Player: {self.name}, Level: {self.lvl}, Exp: {self.exp}/{self.exp_for_lvl}, Max HP: {self.max_hp}, Current HP: {self.current_hp}, Rounds to get ready: " \
            f"{self.rounds_stunned}"

    @abstractmethod
    def act(self, other):
        '''
        Uses action of character
        '''
        pass

    @staticmethod
    def check_if_dead(other):
        """
        Checks if attacked opponent is dead after attack on him, if yes delete it from the team
        :param other: opponent object
        """
        if other.current_hp < 0:  # checks if attack killed opponent
            other.team.team.remove(other)  # deletes dead character from its team

    def get_exp(self):
        self.exp += 250

        if self.exp > self.exp_for_lvl:
            self.exp_for_lvl = 5 * (250 * self.lvl)
            self.lvl += 1
            self.lvl_up()

    def lvl_up(self):
        self.max_hp += 300 * self.lvl
        # if self.rounds_stunned > 0:
        #     self.rounds_stunned -= 1
        # if self.rounds_poisoned > 0:
        #     self.rounds_poisoned -= 1


class Warrior(Character):
    def __init__(self, attack_power, name):
        """
        Creates warrior character object
        :param attack_power: int, damage that character deals
        :param name: str, name of character
        """
        Character.__init__(self, 1300, name)

        self.attack_power = attack_power + random.randint(0, 100)

    def act(self, other):
        self.attack(other)
        self.check_if_dead(other)

    def attack(self, other):
        """
        Skill of character, deals damage to opponent
        :param other: opponent character object
        """
        other.current_hp -= int(self.attack_power * (1 + self.lvl * 0.1))


class Sorceress(Character):
    def __init__(self, attack_power, name):
        """
        Creates sorceress character object
        :param name: str, name of character
        """
        Character.__init__(self, 900, name)

    def act(self, other):
        self.stun(other)
        other.rounds_stunned += 1

    @staticmethod
    def stun(other):
        """
        Skill of character, stuns opponent
        :param other: opponent character object
        """
        other.stunned = True


class Support(Character):
    '''
    Creates support character object
    '''

    def __init__(self, healing_power, name):
        """
        :param healing_power: int, hp that character regenerates
        :param name: str, name of character
        """
        self.name = name
        Character.__init__(self, 800, name)
        self.healing_power = healing_power

    def act(self, other):

        self.heal(other)

    def heal(self, other):
        """
        Heals character from own team - healing_power tells how much it heals
        :param other: character object, from own team
        """
        min(other.current_hp + self.healing_power, other.max_hp)


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
