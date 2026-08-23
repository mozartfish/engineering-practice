from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []

        nums.sort()
        for index, val in enumerate(nums):
            if val > 0:
                break
            if index > 0 and val == nums[index - 1]:
                continue

            start = index + 1
            end = len(nums) - 1

            while start < end:
                threeSum = val + nums[start] + nums[end]
                if threeSum > 0:
                    end -= 1
                elif threeSum < 0:
                    start += 1
                else:
                    result.append([val, nums[start], nums[end]])
                    start += 1
                    end -= 1
                    while nums[start] == nums[start - 1] and start < end:
                        start += 1
        return result
