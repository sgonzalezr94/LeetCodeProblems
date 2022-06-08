# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[j]:
                nums[j + 1] = nums[i]
                j += 1
        return j + 1


# Runtime: 130 ms, faster than 49.94% of Python3 online submissions for Remove Duplicates from Sorted Array.
# Memory Usage: 15.5 MB, less than 96.22% of Python3 online submissions for Remove Duplicates from Sorted Array.
