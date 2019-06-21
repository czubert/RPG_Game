class Team:
    def __init__(self):
        self.team = []

    def __str__(self):
        team_characters = ' \n'.join([element.__str__() for element in self.team])
        return team_characters

    def add_character(self, character):
        self.team.append(character)
        character.team = self

    def __getitem__(self, item):
        return self.team.__getitem__(item)

    def __len__(self):
        return len(self.team)

