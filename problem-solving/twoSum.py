from collections import defaultdict
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numStore = defaultdict(int)

        for indx, val in enumerate(nums):
            diff = target - val
            if diff in numStore:
                return [numStore[diff], indx]
            else:
                numStore[val] = indx
        return []
