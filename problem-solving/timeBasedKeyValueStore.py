from collections import defaultdict


class TimeMap:
    def __init__(self):
        self.timeStore = defaultdict(list)  

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeStore[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        result = ""
        values = self.timeStore.get(key, [])

        lo = 0
        hi = len(values) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if values[mid][1] <= timestamp:
                result = values[mid][0]
                lo = mid + 1
            else:
                hi = mid - 1

        return result
