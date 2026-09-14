from __future__ import annotations


class SolutionKys:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        # brute-force whopping O(n^3)
        # good solution probably have sorting as first step

        subset = [[], []]
        subsets = []
        def getSubsets(intervals, idx, count, limit=4):
            if count >= limit or idx >= len(intervals):
                # without .copy() method .pop() just erases lists from subsets
                subsets.append([subset[0].copy(), subset[1].copy()])
                return

            subset[0].append(idx)
            subset[1].append(intervals[idx])
            getSubsets(intervals, idx + 1, count + 1)

            subset[0].pop()
            subset[1].pop()
            getSubsets(intervals, idx + 1, count)

        getSubsets(intervals, 0, 0)
        subsets = subsets[:-1]
        max_score = -1
        best_comb_ids = []

        # each comb is [[ids], [intervals]]
        for i in range(len(subsets)):

            score = 0
            intervals = []
            intersect = False
            for j in range(len(subsets[i][1])):

                score += subsets[i][1][j][2]
                for left, right in intervals:
                    if left <= subsets[i][1][j][1] and subsets[i][1][j][0] <= right:
                        intersect = True
                        break

                intervals.append([subsets[i][1][j][0], subsets[i][1][j][1]])
                if intersect:
                    break

            if not intersect and score > max_score:
                if len(best_comb_ids) == 0:
                    max_score = score
                    best_comb_ids = subsets[i][0]
                elif score > max_score or (score == max_score and
                                           (len(subsets[i][0]) < len(best_comb_ids) or
                                            subsets[i][0].__str__() < best_comb_ids.__str__())):
                    max_score = score
                    best_comb_ids = subsets[i][0]

        return best_comb_ids


class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        order = sorted(range(n), key=lambda i: intervals[i][1])
        rights = [intervals[i][1] for i in order]


s = Solution()
print(s.maximumWeight([[1,3,2],[4,5,2],[1,5,5],[6,9,3],[6,7,1],[8,9,1]]))  # [2,3]
print(s.maximumWeight([[17,17,10],[23,23,23],[3,8,31],[17,21,48],[18,24,44]]))  # [1,2,3]
print(s.maximumWeight([[7,9,37],[20,24,36],[10,11,28],[23,25,19],[4,21,31],[1,3,9],[11,18,27],[25,25,40]]))  # [0,1,2,7]
