# https://leetcode.com/problems/longest-substring-without-repeating-characters/


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        checked = set()
        for start_idx in range(len(s)):
            checked.clear()
            end_idx = start_idx
            while end_idx < len(s):
                if s[end_idx] in checked:
                    break
                checked.add(s[end_idx])
                end_idx += 1
            max_len = max(max_len, end_idx - start_idx)
        return max_len


# Runtime: 616 ms, faster than 12.65% of Python3 online submissions for Longest Substring Without Repeating Characters.
# Memory Usage: 14.1 MB, less than 49.10% of Python3 online submissions for Longest Substring Without Repeating Characters.
