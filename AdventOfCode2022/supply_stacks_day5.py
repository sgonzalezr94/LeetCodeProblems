from typing import List
from json import loads
import re


class Solution:
    def __init__(self, day: int) -> None:
        self.day_number = day
        self.stacks = []
        self.movements = []

    def __read_file(self):
        with open(f"inputs/{self.day_number}.txt", "r") as file:
            file_data = file.read()
            definition, moves = file_data.split("\n\n")
            containers = []

            for line in definition.split("\n")[:-1]:
                replace = " [0]"

                if line[0] == " ":
                    replace = "[0] "

                containers.append(line.replace("    ", replace).split())

            max_len = max([len(line) for line in containers])

            for line in containers:
                t = max_len - len(line)
                if t > 0:
                    line += ["[0]"] * t
            t = []

            for i in range(len(containers[0])):
                y = []
                for j in range(len(containers)):
                    if containers[j][i] != "[0]":
                        y.append(containers[j][i])
                t.append(y)

            pattern = r"^move (\d+) from (\d+) to (\d+)$"
            instruction_list = [
                list(map(lambda x: int(x), re.findall(pattern, line)[0]))
                for line in moves.strip().split("\n")
            ]
            self.stacks = t
            self.movements = instruction_list
            return t, instruction_list

    def supply_stacks_arrangement(self, reverse) -> str:
        self.__read_file()
        for instruction in self.movements:
            quantity, src_stack, target_stack = instruction
            moved_stack = self.stacks[src_stack - 1][:quantity]

            if reverse:
                moved_stack.reverse()

            self.stacks[target_stack - 1] = moved_stack + self.stacks[target_stack - 1]
            self.stacks[src_stack - 1] = self.stacks[src_stack - 1][quantity:]

        return (
            "".join([line[0] for line in self.stacks]).replace("[", "").replace("]", "")
        )


sol = Solution(5)
b = sol.supply_stacks_arrangement(True)
print(b)
