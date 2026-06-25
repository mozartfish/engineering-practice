from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda pair: pair[0])
        result = [intervals[0]]
        for start, end in intervals:
            currentEnd = result[-1][1]
            if start <= currentEnd:
                result[-1][1] = max(end, currentEnd)
            else:
                result.append([start, end])

        return result
