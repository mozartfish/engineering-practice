from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        numIndx = dict()

        for indx, num in enumerate(nums):
            diff = target - num
            if diff in numIndx:
                diffIndx = numIndx[diff]
                return [diffIndx, indx]
            else:
                numIndx[num] = indx

        return result
