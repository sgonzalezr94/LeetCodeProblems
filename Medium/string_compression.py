# https://leetcode.com/problems/string-compression/
from typing import List
from collections import OrderedDict


TEST = ["a", "a", "a", "b", "b", "a", "a"]
TEST2 = ["a", "a", "b", "b", "c", "c", "c"]
TEST3 = ["a"]
TEST4 = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
TEST5 = ["a", "a", "a", "a", "b", "a"]


class Solution:
    def compress(self, chars: List[str]) -> int:
        od = OrderedDict()
        initialidx = 0
        while initialidx != len(chars):
            if chars[initialidx] not in od:
                od[chars[initialidx]] = 1
            else:
                od[chars[initialidx]] += 1
                chars.remove(chars[initialidx])
                initialidx -= 1
            initialidx += 1

        for key, value in od.items():
            index = chars.index(key)
            if len(str(value)) > 1:
                for number in str(value):
                    chars.insert(index + 1, number)
                    index += 1
            elif value != 1:
                chars.insert(index + 1, str(value))
        print(chars)
        return len(chars)

    def secondcompress(self, chars: List[str]) -> int:
        idx = 0
        current_char = chars[idx]
        counter = 0
        while idx != len(chars):
            if current_char == chars[idx]:
                counter += 1
                chars.pop(idx)
            else:
                chars.insert(idx, current_char)
                idx += 1
                if counter != 1:
                    if counter < 10:
                        chars.insert(idx, str(counter))
                        idx += 1
                    else:
                        chars = self.splitcounter(chars, idx, counter)
                counter = 0
                current_char = chars[idx]
        if len(chars) > 1 and chars[idx - 1] == current_char:
            chars.pop(idx - 1)
            counter += 1
        chars.insert(idx, current_char)
        idx += 1
        if counter != 1:
            if counter < 10:
                chars.insert(idx, str(counter))
            else:
                chars = self.splitcounter(chars, idx, counter)
        print(chars)
        return len(chars)

    def splitcounter(self, chars: List[str], idx: int, counter: int) -> None:
        for strnumber in str(counter):
            chars.insert(idx, strnumber)
            idx += 1
        return chars


sol = Solution()
sol.secondcompress(chars=TEST5)
