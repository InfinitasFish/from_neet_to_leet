from __future__ import annotations


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # to get rid of duplicates we sort nums beforehand, and skipping duplicates in sorted arr is trivial
        # O(n * 2^n) btw, but there's no faster solution
        candidates = sorted(candidates)

        res = []
        def dfs(idx, set, sum):
            if sum == target:
                res.append(set)
                return
            if idx >= len(candidates) or sum > target:
                return

            cand = candidates[idx]
            step = 1
            dfs(idx + step, set + [cand], sum + cand)

            # we take first unique element, search for combinations, only then skip duplicates
            while idx < len(candidates) - step and candidates[idx + step] == cand:
                step += 1
            dfs(idx + step, set, sum)

        dfs(0, [], 0)
        return res


s = Solution()
print(s.combinationSum2([3,3,3], 9))  # [3,3,3]
print(s.combinationSum2([9,2,2,4,6,1,5], 8))  # [[1,2,5],[2,2,4],[2,6]]
print(s.combinationSum2([1,2,3,4,5], 7))  # [[1,2,4],[2,5],[3,4]]
