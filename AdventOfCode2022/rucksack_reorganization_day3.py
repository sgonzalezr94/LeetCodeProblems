from typing import List


class Solution:
    def __init__(self, char_total_str: str, day_number: int) -> None:
        self.char_total_str = char_total_str
        self.day_number = day_number

    def __get_priority(self, character: str) -> int:
        return self.char_total_str.index(character) + 1

    def __extract_item_type(self, characters_string: str) -> str:
        first_half_set = set(characters_string[0 : len(characters_string) // 2])
        second_half_set = set(characters_string[len(characters_string) // 2 :])
        return first_half_set.intersection(second_half_set).pop()

    def __extract_item_type_per_group(self, characters_strings_list: List[str]) -> str:
        first_half_set = set(characters_strings_list[0])
        second_half_set = set(characters_strings_list[1])
        third_half_set = set(characters_strings_list[2])
        a = first_half_set.intersection(second_half_set).intersection(third_half_set)
        # print(a, self.__get_priority(a.pop()))
        return (
            first_half_set.intersection(second_half_set)
            .intersection(third_half_set)
            .pop()
        )

    def total_priorities_sum(self, day_number: int) -> set:
        with open(f"inputs/{day_number}.txt", "r") as input:
            total_sum = 0
            for line in input.readlines():
                total_sum += self.__get_priority(self.__extract_item_type(line.strip()))
        return total_sum

    def total_priorities_sum_per_group(self, day_number: int) -> set:
        with open(f"inputs/{day_number}.txt", "r") as input:
            total_sum = 0
            tmp_list = list()
            for idx, line in enumerate(input.readlines()):
                if idx % 3 == 0 and idx != 0:
                    print(tmp_list)
                    total_sum += self.__get_priority(
                        self.__extract_item_type_per_group(tmp_list)
                    )
                    tmp_list = []
                    tmp_list.append(line.strip())

                else:
                    tmp_list.append(line.strip())
            # We need to do this to include the last triplet since idx % 3 == 0 and idx != 0 validation can't be performed anymore
            total_sum += self.__get_priority(
                self.__extract_item_type_per_group(tmp_list)
            )
        return total_sum


CHARS_STR = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
sol = Solution(char_total_str=CHARS_STR, day_number=3)
ans = sol.total_priorities_sum_per_group(sol.day_number)
# 2363
