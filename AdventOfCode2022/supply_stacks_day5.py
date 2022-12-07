from typing import List
from json import loads


class Solution:
    def __init__(self, day: int) -> None:
        self.day_number = day
        self.stacks_dict = dict()
        self.movements = list()

    def _read_input(self):
        with open(f"inputs/{self.day_number}.txt", "r") as input:
            data = [line.strip().split() for line in input.readlines()]
            stack_positions, movements = data[0:8], data[10:]
            self.__create_stack_dict(stack_positions)
            self.movements = movements

    def __create_stack_dict(self, stack_configuration: List[str]):
        self.stacks_dict = {idx: list() for idx in range(len(stack_configuration[0]))}
        for stack_column in stack_configuration:
            self.stacks_dict[0].append(stack_column[0])
            self.stacks_dict[1].append(stack_column[1])
            self.stacks_dict[2].append(stack_column[2])
            self.stacks_dict[3].append(stack_column[3])
            self.stacks_dict[4].append(stack_column[4])
            self.stacks_dict[5].append(stack_column[5])
            self.stacks_dict[6].append(stack_column[6])
            self.stacks_dict[7].append(stack_column[7])
            self.stacks_dict[8].append(stack_column[8])
        for dict in self.stacks_dict:
            self.stacks_dict[dict].reverse()

    def __move_elements_from_stack(
        self, number_of_elements: int, from_stack: int, to_stack: int
    ) -> dict:
        for _ in range(number_of_elements):
            try:
                self.stacks_dict[to_stack - 1].append(
                    self.stacks_dict[from_stack - 1].pop()
                )
            except Exception as e:
                print(e)

        return self.stacks_dict

    def supply_stacks_arrangement(self) -> str:
        print(self.movements)
        for movement in self.movements:
            self.__move_elements_from_stack(
                int(movement[1]), int(movement[3]), int(movement[5])
            )
        print(self.stacks_dict)
        response = ""
        for stack in self.stacks_dict:
            response += self.stacks_dict[stack].pop()[1]
        response = response.replace("0", "")
        print(response)
        return response


sol = Solution(5)
data = sol._read_input()
sol.supply_stacks_arrangement()
# print(data[0], len(data[0]), data[0].split())
