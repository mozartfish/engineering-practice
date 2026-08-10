from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for indx, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stackTemp, stackIndx = stack.pop()
                result[stackIndx] = indx - stackIndx
            stack.append((temp, indx))

        return result
