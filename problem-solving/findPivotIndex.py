from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_pivot = -1
        total = sum(nums)
        leftSum = 0
        for i in range(len(nums)):
            rightSum = total - nums[i] - leftSum
            if leftSum == rightSum:
                left_pivot = i
                return left_pivot
            leftSum += nums[i]

        return left_pivot
