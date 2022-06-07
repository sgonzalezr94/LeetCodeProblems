# https://leetcode.com/problems/roman-to-integer/


class Solution:
    roman_symbol_dictionary = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }
    roman_special_instances_dict = {
        "IV": 4,
        "IX": 9,
        "XL": 40,
        "XC": 90,
        "CD": 400,
        "CM": 900,
    }

    def romanToInt(self, s: str) -> int:
        number = 0
        for special_instance in self.roman_special_instances_dict:
            if special_instance in s:
                number += self.roman_special_instances_dict[special_instance]
                s = s.replace(special_instance, "")
        for symbol in s:
            number += self.roman_symbol_dictionary[symbol]
        return number


# Runtime: 40 ms, faster than 98.06% of Python3 online submissions for Roman to Integer.
# Memory Usage: 13.9 MB, less than 29.65% of Python3 online submissions for Roman to Integer.
