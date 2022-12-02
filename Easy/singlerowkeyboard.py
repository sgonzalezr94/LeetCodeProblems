# https://leetcode.com/problems/single-row-keyboard/


class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        cost = 0
        prev_idx = 0
        for character in word:
            current_idx = keyboard.index(character)
            cost += abs(prev_idx - current_idx)
            prev_idx = current_idx
        return cost


keyboard = "abcdefghijklmnopqrstuvwxyz"
word = "cba"

sol = Solution()
sol.calculateTime(keyboard, word)

# Runtime: 47 ms, faster than 94.41% of Python3 online submissions for Single-Row Keyboard.
