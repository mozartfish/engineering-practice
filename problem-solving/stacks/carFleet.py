from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        carInfo = [(p, v) for p, v in zip(position, speed)]
        stack = []

        carInfo.sort(reverse=True)
        for p, v in carInfo:
            stack.append((target - p) / v)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)
