from typing import List


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start = 0
        end = len(heights) - 1
        result = 0

        while start < end:
            area = min(heights[start], heights[end]) * (end - start)
            result = max(result, area)
            if heights[start] <= heights[end]:
                start += 1
            else:
                end -= 1
        return result
