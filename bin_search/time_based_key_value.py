from __future__ import annotations
from collections import defaultdict


# `All the timestamps timestamp of set are strictly increasing.`
class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.map[key]
        left = 0
        right = len(values) - 1
        while left <= right:
            mid = (left + right) // 2
            # to find max `prev_timestamp <= timestamp`, move left
            if values[mid][0] <= timestamp:
                res = values[mid][1]
                left = mid + 1
            else:
                right = mid - 1

        return res


tm = TimeMap()
tm.set("love", "high", 10)
tm.set("love", "low", 20)
print(tm.get("love", 5))
print(tm.get("love", 10))
print(tm.get("love", 15))