# https://leetcode.com/problems/permutations/description/
from typing import List


class Solution:
    def calculate_permutations(self, numbers_list: List[int]) -> List[List[int]]:
        if len(numbers_list) == 1:
            return [numbers_list[:]]
        
        ans = []

        for _ in range(len(numbers_list)):
            first_number = numbers_list.pop(0)
            permutations = self.calculate_permutations(numbers_list)

            for permutation in permutations:
                permutation.append(first_number)
            
            ans.extend(permutations)
            numbers_list.append(first_number)
        
        return ans
    
sol = Solution()
print(sol.calculate_permutations([1,2,3]))