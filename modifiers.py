class Modifier:
    def __init__(self, caster, target, duration: int) -> None:
        self.caster = caster
        self.target = target
        self.duration = duration

    def act(self) -> None:
        pass


class Stun(Modifier):
    def __init__(self, caster, target, duration: int) -> None:
        Modifier.__init__(self, caster, target, duration)
        self.mana_cost = 100
        self.duration = duration

    def act(self) -> None:
        self.stun()

    def stun(self) -> None:
        if self.duration > 0:
            self.target.next_move = self.target.do_nothing
            self.duration -= 1
        else:
            self.target.next_move = self.target.act
            self.target.modifier_list.remove(self)


class Poison(Modifier):
    def __init__(self, caster, target, duration: int, damage: int) -> None:
        Modifier.__init__(self, caster, target, duration)
        self.damage = damage
        self.mana_cost = 150

    def act(self) -> None:
        self.poison()

    def poison(self) -> None:
        if self.duration > 0:
            self.target.current_hp -= self.damage
            self.caster.remove_if_dead(self.target)
            self.duration -= 1
        else:
            self.target.modifier_list.remove(self)

# class LuckyShot(Modifier):
#     @staticmethod
#     # TODO: make lucky shot a parameter of character, so every character has it's own different lucky chance
#     def lucky_shot() -> bool:
#         if random.randrange(0, 10, 1) <= 1:
#             return True
#         else:
#             return False
