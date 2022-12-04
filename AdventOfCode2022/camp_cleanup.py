# https://adventofcode.com/2022/day/4
from typing import List


class Solution:
    def __init__(self, day_number) -> None:
        self.day_number = day_number
        self.list_of_pairs = self._read_input(self.day_number)

    def _read_input(self, day_number: int = 4) -> List[str]:
        with open(f"inputs/{day_number}.txt", "r") as input:
            return [line.strip() for line in input.readlines()]

    def _is_contained(self, pairs_string: str) -> bool:
        pair_1, pair_2 = pairs_string.split(",")
        pair_1 = list(map(int, pair_1.split("-")))
        pair_2 = list(map(int, pair_2.split("-")))
        if (pair_1[0] <= pair_2[0] and pair_1[1] >= pair_2[1]) or (
            pair_2[0] <= pair_1[0] and pair_2[1] >= pair_1[1]
        ):
            return True
        else:
            return False

    # 2-6,4-8
    def _is_overlapped(self, pairs_string: str) -> bool:
        pair_1, pair_2 = pairs_string.split(",")
        pair_1 = list(map(int, pair_1.split("-")))
        pair_2 = list(map(int, pair_2.split("-")))
        if (
            (pair_2[0] <= pair_1[0] <= pair_2[1])
            or (pair_2[0] <= pair_1[1] <= pair_2[1])
            or (pair_1[0] <= pair_2[0] <= pair_1[1])
            or (pair_1[0] <= pair_2[1] <= pair_1[1])
        ):
            return True
        else:
            return False

    def scan_contained_pairs(self, pairs_list: List[str]) -> int:
        if not pairs_list:
            contained_pairs = [
                self._is_contained(string_pair) for string_pair in self.list_of_pairs
            ].count(True)
        else:
            contained_pairs = [
                self._is_contained(string_pair) for string_pair in self.list_of_pairs
            ].count(True)
        return contained_pairs

    def scan_overlapped_pairs(self, pairs_list: List[str]) -> int:
        if not pairs_list:
            over_lapped_pairs = [
                self._is_overlapped(string_pair) for string_pair in self.list_of_pairs
            ].count(True)
        else:
            over_lapped_pairs = [
                self._is_overlapped(string_pair) for string_pair in self.list_of_pairs
            ].count(True)
        return over_lapped_pairs


sol = Solution(4)
contained_ans = sol.scan_contained_pairs(sol.list_of_pairs)
overlapped_ans = sol.scan_overlapped_pairs(sol.list_of_pairs)

# 433
# 852
# That's the right answer! You are one gold star closer to collecting enough star fruit. Yay!
# You have completed Day 4! You can [Share] this victory
