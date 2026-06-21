from typing import List


class NumArray:
    def __init__(self, nums: List[int]):
        self.prefixSum = []
        total = 0
        for num in nums:
            total += num
            self.prefixSum.append(total)

    def sumRange(self, left: int, right: int) -> int:
        preRight = self.prefixSum[right]
        preLeft = 0
        if left > 0:
            preLeft = self.prefixSum[left - 1]

        result = preRight - preLeft
        return result


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
