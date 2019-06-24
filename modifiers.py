class Modifier:
    def __init__(self, caster, target, duration, damage=0):
        self.caster = caster
        self.target = target
        self.duration = duration
        self.damage = damage

    def act(self):
        pass


class Stun(Modifier):
    def act(self):
        self.stun()

    def stun(self):
        if self.duration > 0:
            self.target.next_move = self.target.do_nothing
            self.duration -= 1
        else:
            self.target.next_move = self.target.act
            self.target.modifier_list.remove(self)


class Poison(Modifier):
    def act(self):
        self.poison()

    def poison(self):
        if self.duration > 0:
            self.target.current_hp -= self.damage
            self.duration -= 1
            print(f"poisoned, damage {self.damage}, duration: {self.duration}")
        else:
            self.target.next_move = self.target.act
            self.target.modifier_list.remove(self)
