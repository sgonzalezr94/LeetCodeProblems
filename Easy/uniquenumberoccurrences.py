# https://leetcode.com/problems/unique-number-of-occurrences/

from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurrences_dict = dict()
        for number in arr:
            if number not in occurrences_dict:
                occurrences_dict[number] = 1
            else:
                occurrences_dict[number] += 1
        occurences_values = dict()
        for occurence in occurrences_dict.values():
            if occurence not in occurences_values:
                occurences_values[occurence] = True
        return len(occurrences_dict.values()) == len(occurences_values)


arr = [1, 2, 2, 1, 1, 3]

solution = Solution()
ans = solution.uniqueOccurrences(arr)
assert ans
