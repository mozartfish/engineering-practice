from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        start = 0
        end = len(height) - 1
        result = 0
        maxLeftHeight = height[start]
        maxRightHeight = height[end]

        while start < end:
            if maxLeftHeight < maxRightHeight:
                start += 1
                maxLeftHeight = max(maxLeftHeight, height[start])
                result += maxLeftHeight - height[start]
            else:
                end -= 1
                maxRightHeight = max(maxRightHeight, height[end])
                result += maxRightHeight - height[end]

        return result
