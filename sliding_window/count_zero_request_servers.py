from __future__ import annotations

from itertools import count


class Solution_:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        # [server_id, time]
        # [queries[i] - x, queries[i]]
        # O(n*m), doesn't pass
        res = []
        servers = set([id_time[0] for id_time in logs])
        # not all servers can be mentioned in logs, like in first test case
        diff = n - len(servers)

        for query in queries:
            servers_ = servers.copy()
            left = query - x
            for id_time in logs:
                if id_time[0] in servers_ and left <= id_time[1] <= query:
                    servers_.remove(id_time[0])

            res.append(len(servers_) + diff)

        return res


class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs = sorted(logs, key=lambda it: it[1])
        queries = sorted((t, i) for i, t in enumerate(queries))
        counts = [0] * (n + 1)
        l = r = active = 0
        res = [0] * len(queries)

        for t, i in queries:
            # count all as active up to T
            while r < len(logs) and logs[r][1] <= t:
                ids = logs[r][0]
                counts[ids] += 1
                if counts[ids] == 1:
                    active += 1
                r += 1

            # decrement active that are not in T - x
            while l < r and logs[l][1] < t - x:
                ids = logs[l][0]
                counts[ids] -= 1
                if counts[ids] == 0:
                    active -= 1
                l += 1

            res[i] = n - active

        return res


s = Solution()
print(s.countServers(3, [[1,3],[2,6],[1,5]], 5, [10, 11]))  # [1, 2]
print(s.countServers(3, [[2,4],[2,1],[1,2],[3,1]], 2, [3,4]))  # [0, 1]
