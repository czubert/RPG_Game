class Team:
    def __init__(self, name):
        """

        :param name:
        """
        self.name = name
        self.team = []

    def __str__(self):
        """

        :return:
        """
        team_characters = ' \n'.join([element.__str__() for element in self.team])

        return team_characters

    def add_character(self, character):
        """

        :param character:
        """
        self.team.append(character)
        character.team = self

    def __getitem__(self, item):
        """

        :param item:
        :return:
        """
        return self.team.__getitem__(item)

    def __len__(self):
        """

        :return:
        """
        return len(self.team)

