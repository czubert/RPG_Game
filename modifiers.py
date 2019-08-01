class Modifier:
    def __init__(self, caster, target, duration):
        self.caster = caster
        self.target = target
        self.duration = duration

    def act(self):
        pass


class Stun(Modifier):
    def __init__(self, caster, target, duration):
        Modifier.__init__(self, caster, target, duration)
        self.mana_cost = 100
        self.duration = duration

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
        self.mana_cost = 150

    def act(self):
        self.poison()

    def poison(self):
        if self.duration > 0:
            self.target.current_hp -= self.damage
            self.caster.remove_if_dead(self.target)
            self.duration -= 1
        else:
            self.target.modifier_list.remove(self)

# class LuckyShot(Modifier):
#     @staticmethod
#     # TODO: make lucky shot a parameter of character, so every character has it's own different lucky chance
#     def lucky_shot():
#         if random.randrange(0, 10, 1) <= 1:
#             return True
#         else:
#             return False
