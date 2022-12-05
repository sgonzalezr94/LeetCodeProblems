from typing import List


class Solution:
    def __init__(self, selection_values_dict: dict, day: int = 2) -> None:
        self.moves_dict = selection_values_dict
        self.day = day
        self.games_list = list()

    def _read_input(self, day: int) -> List[List[str]]:
        with open(f"inputs/{day}.txt", "r") as input:
            self.games_list = [line.strip().split(" ") for line in input.readlines()]
            return self.games_list

    def compare_selections_st1(self, selection: List[str]):
        points = 0
        if self.moves_dict[selection[0]][0] == selection[1]:
            points = self.moves_dict[selection[1]][3] + 6

        elif self.moves_dict[selection[0]][1] == selection[1]:
            points = self.moves_dict[selection[1]][3] + 3
        else:
            points = self.moves_dict[selection[1]][3]
        return points

    def compare_selections_st2(self, selection: List[str]):
        points = 0
        if selection[1] == "X":
            points = self.moves_dict[self.moves_dict[selection[0]][2]][3]

        elif selection[1] == "Y":
            points = self.moves_dict[self.moves_dict[selection[0]][1]][3] + 3
        else:
            points = self.moves_dict[self.moves_dict[selection[0]][0]][3] + 6
        return points

    def total_score_partial_strategy(self, selections_list: List[List[str]]):
        total_score = 0
        for selection in selections_list:
            total_score += self.compare_selections_st1(selection)
        return total_score

    def total_score_complete_strategy(self, selections_list: List[List[str]]):
        total_score = 0
        for selection in selections_list:
            total_score += self.compare_selections_st2(selection)
        return total_score


MOVES_DICT = {
    "A": ("Y", "X", "Z", 1),
    "B": ("Z", "Y", "X", 2),
    "C": ("X", "Z", "Y", 3),
    "X": ("B", "A", "C", 1),
    "Y": ("C", "B", "A", 2),
    "Z": ("A", "C", "B", 3),
}


sol = Solution(selection_values_dict=MOVES_DICT)
sol._read_input(sol.day)
sol.total_score_partial_strategy(sol.games_list)  # 10718
sol.total_score_complete_strategy(sol.games_list)  # 14652

# You have completed Day 2!
