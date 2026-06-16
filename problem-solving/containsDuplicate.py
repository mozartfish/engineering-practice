from typing import List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_set = set()
        for indx, num in enumerate(nums):
            if num not in num_set:
                num_set.add(num)
            else:
                return True

        return False
