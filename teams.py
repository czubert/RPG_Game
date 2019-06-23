class Team:
    def __init__(self, name):
        self.name = name
        self.team = []

    def __str__(self):
        return ' \n'.join([element.__str__() for element in self.team])

    def add_character(self, character):
        '''
        Adds character to a team and links character with it's team
        :param character: Character object
        '''
        self.team.append(character)
        character.team = self

    def __getitem__(self, item):
        return self.team.__getitem__(item)

    def __len__(self):
        return len(self.team)
