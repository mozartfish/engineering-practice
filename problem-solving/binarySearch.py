from typing import List


def search(self, nums: List[int], target: int) -> int:
    def binarySearch(lo, hi, nums, target):
        if lo > hi:
            return -1

        mid = lo + (hi - lo) // 2

        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            return binarySearch(mid + 1, hi, nums, target)
        if nums[mid] > target:
            return binarySearch(lo, mid - 1, nums, target)

    return binarySearch(0, len(nums) - 1, nums, target)


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums) - 1

        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                lo = mid + 1
            if nums[mid] > target:
                hi = mid - 1

        return -1
