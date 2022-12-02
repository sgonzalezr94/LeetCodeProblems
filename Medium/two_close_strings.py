# https://leetcode.com/problems/determine-if-two-strings-are-close/


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        fq_w1 = dict()
        fq_w2 = dict()
        i = 0
        while i < len(word1):
            if word1[i] not in word2 or word2[i] not in word1:
                return False
            if word1[i] not in fq_w1:
                fq_w1[word1[i]] = 1
            else:
                fq_w1[word1[i]] += 1
            if word2[i] not in fq_w2:
                fq_w2[word2[i]] = 1
            else:
                fq_w2[word2[i]] += 1
            i += 1
        return sorted(fq_w1.values()) == sorted(fq_w2.values())


word1 = "cabbba"
word2 = "abbccc"
expected = True
sol = Solution()
ans = sol.closeStrings(word1, word2)

# 456 ms, faster than 32.40% of Python3 online submissions for Determine if Two Strings Are Close.

# TODO Must optimize it
