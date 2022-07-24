# https://leetcode.com/problems/remove-element/

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while True:
            try:
                nums.remove(val)
            except ValueError:
                break


# Runtime: 60 ms, faster than 29.75% of Python3 online submissions for Remove Element.
# Memory Usage: 14 MB, less than 14.31% of Python3 online submissions for Remove Element.
