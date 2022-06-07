# https://leetcode.com/problems/palindrome-number/
# An integer is a palindrome when it reads the same backward as forward.


class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        i = 0
        j = len(x) - 1
        while i <= j:
            if x[i] != x[j]:
                return False
            i += 1
            j -= 1
        return True


# Runtime: 82 ms, faster than 58.11% of Python3 online submissions for Palindrome Number.
# Memory Usage: 13.8 MB, less than 96.58% of Python3 online submissions for Palindrome Number.
