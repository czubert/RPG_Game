class Modifier:
    def __init__(self, caster, target, duration):
        self.caster = caster
        self.target = target
        self.duration = duration

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
    def __init__(self, caster, target, duration, damage):
        Modifier.__init__(self, caster, target, duration)
        self.damage = damage

    def act(self):
        self.poison()

    def poison(self):
        if self.duration > 0:
            self.target.current_hp -= self.damage
            self.caster.remove_if_dead(self.target)
            self.duration -= 1
        else:
            self.target.modifier_list.remove(self)
