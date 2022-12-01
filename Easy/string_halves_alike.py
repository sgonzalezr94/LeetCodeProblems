# https://leetcode.com/problems/determine-if-string-halves-are-alike/


class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = "aeiou"
        string_list = list(s.lower())
        first_half = 0
        second_half = 0
        for character in string_list[0 : len(string_list) // 2]:
            if character in vowels:
                first_half += 1
        for character in string_list[len(string_list) // 2 :]:
            if character in vowels:
                second_half += 1
        return first_half == second_half


s = "textbook"
solution = Solution()
answer = solution.halvesAreAlike(s)

# 32 ms, faster than 98.12% of Python3 online submissions for Determine if String Halves Are Alike.
