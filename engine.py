import time
import itertools

from teams import Team
from characters import *


class Engine:
    def __init__(self, team1_size: int, team2_size: int) -> None:
        self.teams_list = []
        self.rounds = 0
        self.program_execution_time = 0
        self.team1_size = team1_size
        self.team2_size = team2_size
        self.set_teams(team1_size, team2_size)

    def create_new_team(self, name: str) -> Team:
        """
        Creates Team and sets it's name
        :param name: str
        :return: str, teams name
        """
        tmp_team = Team(name)
        self.teams_list.append(tmp_team)
        return tmp_team

    def set_teams(self, team1_size: int, team2_size: int) -> None:
        # # creates two opposite team objects and gives them names
        team1 = self.create_new_team('New York Gangs')
        team2 = self.create_new_team('Pirates of the Caribbean')

        # # creates characters for both teams and adds them to the teams
        team1.team_generator(team1_size)
        team2.team_generator(team2_size)

        # # now one team is known by the other one
        team1.opponent_team = team2
        team2.opponent_team = team1
        # print(f'team1:{len(team1.team)}, team1 opponents:{len(team1.opponent_team.team)}')

    def run_game(self) -> None:
        start_time = time.time()

        random.shuffle(self.teams_list)  # randoms starting team

        # self.terminate_process()
        self.fight()

        self.program_execution_time = round(time.time() - start_time, 4)

        print(self.battle_summary())

    def fight(self) -> None:
        """
        Takes next character from drawn team to start fight against drawn character from opponents team
        If Character has skills working on your own team it also takes round.
        After attack/support it changes the team to another one.
        :return: Stops attack if chosen character is stunned
        """
        while True:  # works until one team is dead
            # tmp_list = self.teams_list.copy()  # copy of teams list, for generator
            gen_list = [i.find_attacking_character() for i in self.teams_list]
            pair_of_characters = itertools.zip_longest(*gen_list)

            for char_pairs_tuples in pair_of_characters:
                for char in char_pairs_tuples:
                    if char is None:
                        continue
                    else:
                        if any([i.empty for i in self.teams_list]):
                            return
                        char.team.team_act(char)

            #
            # for team in self.teams_list:
            #     team.generator = team.find_attacking_character()  # sets generator 'object'
            #     if team.generator is None:
            #         continue
            #     else:
            #         char = next(team.generator)
            #         if char is None:
            #             self.teams_list.remove(team)
            #         else:
            #             # if team.opponent_team.team:
            #             team.team_act(char)

            # while tmp_list:
            #     for team in tmp_list:
            #         char = next(team.generator)
            #         if char is None:
            #             tmp_list.remove(team)
            #         else:
            #             if team.opponent_team.team:
            #                 team.team_act(char)

            # on round end
            for team in self.teams_list:
                team.after_round_regenerate_mana_and_hp()

                self.rounds += 1  # counts the rounds

    def battle_summary(self) -> str:
        winning_team = list(filter(bool, self.teams_list))

        # return f"Team:{winning_team.name}\n Battle took: {self.rounds} rounds, {self.program_execution_time} s"
        return f"{self.rounds}, {self.program_execution_time}, {winning_team[0].name},"


if __name__ == '__main__':
    # # creates game object based on Engine class
    game = Engine(1000, 50)

    # # starts game
    game.run_game()

    print(game.battle_summary())
