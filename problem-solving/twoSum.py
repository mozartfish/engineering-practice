from collections import defaultdict
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numStore = defaultdict(int)

        for indx, num in enumerate(nums):
            diff = target - num
            if diff in numStore:
                return [numStore[diff], indx]
            else:
                numStore[num] = indx

        return [-1, -1]
