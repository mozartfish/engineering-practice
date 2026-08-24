from typing import List


class Solution:
    def binarySearch(self, start, end, nums, target):
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1

        return -1
        # pass

    def search(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums) - 1

        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid

        pivot = lo

        result = self.binarySearch(0, pivot - 1, nums, target)
        if result != -1:
            return result

        return self.binarySearch(pivot, len(nums) - 1, nums, target)

        # pass
