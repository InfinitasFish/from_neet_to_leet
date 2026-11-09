from __future__ import annotations
from heapq import heapify, heappop, heappush
from statistics import multimode


class Solution_:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        # exceeds time limit
        # keep busy servers
        busy = set()

        # use min-heap to track current tasks
        heap = []
        heapify(heap)

        # use hashmap to calculate finished requests
        counts = {server: 0 for server in range(k)}

        for i in range(len(arrival)):
            while heap and heap[0][0] <= arrival[i]:
                _, server = heappop(heap)
                busy.remove(server)

            server = i % k
            if server not in busy:
                busy.add(server)
                counts[server] += 1
                heappush(heap, [load[i] + arrival[i], server])
                continue

            f = False
            for s in range(server + 1, k):
                if s not in busy:
                    busy.add(s)
                    counts[s] += 1
                    heappush(heap, [arrival[i] + load[i], s])
                    f = True
                    break

            if not f:
                for s in range(server):
                    if s not in busy:
                        busy.add(s)
                        counts[s] += 1
                        heappush(heap, [arrival[i] + load[i], s])
                        break

        max_count = max(counts.items(), key=lambda kv: kv[1])[1]
        return [server for server, count in counts.items() if count == max_count]


class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        free = list(range(k))  # already a heap: each free server is keyed by its next turn

        handled, busy = [], []  # busy: (time it frees up, server)
        for i, (t, d) in enumerate(zip(arrival, load)):
            while busy and busy[0][0] <= t:  # done by time t
                heappush(free, i + (heappop(busy)[1] - i) % k)  # its first turn from i on
            if free:  # otherwise the request is dropped
                x = heappop(free) % k
                heappush(busy, (t + d, x))
                handled.append(x)

        return multimode(handled)


s = Solution()
print(s.busiestServers(3, [1,2,3,4,5], [5,2,3,3,3]))  # [1]
print(s.busiestServers(3, [1,2,3,4], [1,2,1,2]))  # [0]
print(s.busiestServers(3, [1,2,3], [10,11,12]))  # [0,1,2]
print(s.busiestServers(3, [1,2,3,4,8,9,10], [5,2,10,3,1,2,2]))  # [1]
print(s.busiestServers(2, [1,2,3], [1000000000,1,1000000000]))  # [1]
print(s.busiestServers(7, [1,3,4,5,6,11,12,13,15,19,20,21,23,25,31,32],
                       [9,16,14,1,5,15,6,10,1,1,7,5,11,4,4,6]))  # [0]
