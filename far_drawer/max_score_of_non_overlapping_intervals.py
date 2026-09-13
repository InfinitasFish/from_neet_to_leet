from __future__ import annotations


class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        # brute-force whopping O(n^3)
        # good solution probably have sorting as first step

        # don't really have an idea how to keep both indexes of intervals and intervals themselves
        # for now
        def getCombs(intervals, idx):
            combs = []
            return combs

        combs = getCombs(intervals, 0)
        max_score = -1
        best_comb_ids = []
        # each comb is [[ids], [intervals]]
        for i in range(len(combs)):
            print(combs[i])
            score = 0
            intervals = []
            intersect = False
            for j in range(len(combs[i][1])):

                intervals.append([combs[i][1][j][0], combs[i][1][j][1]])
                score += combs[i][1][j][2]
                if score == 0:
                    continue

                for left, right in intervals:
                    if left <= combs[i][1][j][0] <= right or left <= combs[i][1][j][1] <= right:
                        intersect = True
                        break
                    score += combs[i][1][j][2]

                if intersect:
                    break

            if not intersect and score > max_score:
                if len(best_comb_ids) == 0:
                    max_score = score
                    best_comb_ids = combs[i][0]
                elif combs[i][0].__str__() < best_comb_ids.__str__():
                    max_score = score
                    best_comb_ids = combs[i][0]

        return best_comb_ids


s = Solution()
print(s.maximumWeight([[1,3,2],[4,5,2],[1,5,5],[6,9,3],[6,7,1],[8,9,1]]))  # [2,3]

