# https://leetcode.com/problems/valid-parentheses/


class Solution:
    opening_symbols = {"(": 1, "[": 2, "{": 3}
    closing_symbols = {")": 1, "]": 2, "}": 3}

    def isValid(self, s: str) -> bool:
        validation_stack = list()
        for char in s:
            if char in self.opening_symbols:
                validation_stack.append(self.opening_symbols[char])
            else:
                if (
                    validation_stack
                    and validation_stack.pop() == self.closing_symbols[char]
                ):
                    pass
                else:
                    return False
        if not validation_stack:
            return True
        else:
            return False


# Runtime: 43 ms, faster than 52.19% of Python3 online submissions for Valid Parentheses.
# Memory Usage: 13.9 MB, less than 23.45% of Python3 online submissions for Valid Parentheses.
