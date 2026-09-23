from __future__ import annotations


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # to get rid of duplicates we sort nums beforehand, and skipping duplicates in sorted arr is trivial
        # O(n * 2^n) btw, but there's no faster solution
        candidates = sorted(candidates)

        res = []
        def dfs(idx, set, sum):
            if idx >= len(candidates) or sum > target:
                return
            if sum == target:
                res.append(set.copy())
                return

            set.append(candidates[idx])
            dfs(idx + 1, set, sum + candidates[idx])

            set.pop()
            while idx < len(candidates) - 1 and candidates[idx] == candidates[idx + 1]:
                idx += 1
            dfs(idx + 1, set, sum)

        dfs(0, [], 0)
        return res


s = Solution()
print(s.combinationSum2([9,2,2,4,6,1,5], 8))  # [[1,2,5],[2,2,4],[2,6]]
print(s.combinationSum2([1,2,3,4,5], 7))  # [[1,2,4],[2,5],[3,4]]
