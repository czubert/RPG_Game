import random

class Character:
    def __init__(self, max_hp):
        self.max_hp = max_hp
        self.current_hp = self.max_hp
        self.rounds_stunned = 0
        self.team = None

    def __str__(self):
        return f"Max HP: {self.max_hp}, Current HP: {self.current_hp}, Rounds to get ready: {self.rounds_stunned}"

    def act(self):
        pass


class Warrior(Character):
    def __init__(self, attack_power):
        Character.__init__(self, 1200)
        self.attack_power = attack_power + random.randint(0, 100)

    def act(self, other):
        self.attack(other)

    def attack(self, other):
        other.current_hp -= self.attack_power
        if other.current_hp < 0:
            other.team.team.remove(other)
            if len(other.team) == 0:
                print(f"Team: {self.team.name} won the battle")
                quit()


class Sorceress(Character):
    def __init__(self):
        Character.__init__(self, 500)

    def act(self, other):
        self.stun(other)
        other.rounds_stunned += 3

    @staticmethod
    def stun(other):
        other.stunned = True


class Support(Character):
    def __init__(self, healing_power):
        Character.__init__(self, 400)
        self.healing_power = healing_power

    def act(self, other):
        self.heal(other)

    def heal(self, other):
        if other.current_hp + self.healing_power > other.max_hp:
            other.current_hp = other.max_hp
        else:
            other.current_hp += self.healing_power


if __name__ == '__main__':


    war1 = Warrior(300)
    sorc1 = Sorceress()
    supp1 = Support(100)

    war1.act(supp1)
    supp1.act(supp1)

    print(war1.current_hp)
    print(sorc1.current_hp)
    print(supp1.current_hp)

    print(war1)