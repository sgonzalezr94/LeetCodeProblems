# https://leetcode.com/problems/longest-common-prefix/
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = list()
        for letters_tuple in zip(*strs):
            if (
                len(set(letters_tuple)) == 1
            ):  # Basically, if all the characters in the tuple are the same, it's a consistent character to be added to the prefix list.
                prefix.append(letters_tuple[0])
            else:  # When at least one of them isn't equal, the longest prefix has been found.
                break
        return "".join(prefix)


# Runtime: 56 ms, faster than 33.35% of Python3 online submissions for Longest Common Prefix.
# Memory Usage: 14 MB, less than 48.95% of Python3 online submissions for Longest Common Prefix.
