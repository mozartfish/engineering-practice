import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo = 1
        hi = max(piles)
        result = hi

        while lo <= hi:
            k = lo + (hi - lo) // 2
            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p) / k)
            if totalTime <= h:
                result = k
                hi = k - 1
            else:
                lo = k + 1
        return result
