class Character:
    def __init__(self, max_hp):
        self.max_hp = max_hp
        self.current_hp = self.max_hp
        self.stunned = False

    def __str__(self):
        return f"Max HP: {self.max_hp}, Current HP: {self.current_hp}, Stunned: {self.stunned}"

    def act(self):
        pass


class Warrior(Character):
    def __init__(self, attack_power):
        Character.__init__(self, 3200)
        self.attack_power = attack_power

    def act(self, other):
        self.attack(other)

    def attack(self, other):
        other.current_hp -= self.attack_power
        if other.current_hp < 0:
            print("Your hp status is under 0, means you are dead")


class Sorceress(Character):
    def __init__(self):
        Character.__init__(self, 1500)

    def act(self, other):
        self.stun(other)

    @staticmethod
    def stun(other):
        other.stunned = True


class Support(Character):
    def __init__(self, healing_power):
        Character.__init__(self, 900)
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