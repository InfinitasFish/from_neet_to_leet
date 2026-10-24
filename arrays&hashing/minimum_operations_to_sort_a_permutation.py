from __future__ import annotations
from collections import deque


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # check for ascending/descending order
        asc = 1
        dsc = 1
        n = len(nums)

        for i in range(1, n):
            # modulo to not break on zero ([2,0,1] -> ascending)
            asc += nums[i] == (nums[i - 1] + 1) % n
            dsc += nums[i - 1] == (nums[i] + 1) % n

        # two cases:
        # sorted ascending with rotation
        # sorted descending with rotation
        # return -1 otherwise

        if asc == n:
            # two cases, take min:
            # just rotate left
            # reverse, rotate left until 0 is last element, reverse
            if nums[0] == 0:
                return 0
            first = n - nums[0]
            second = nums[0] + 2
            return min(first, second)

        if dsc == n:
            # reverse and get ascending case
            first = 1 + n - nums[-1]
            second = nums[-1] + 1
            return min(first, second)

        return -1


s = Solution()
print(s.minOperations([0,2,1]))  # 2
print(s.minOperations([1,0,2]))  # 2
print(s.minOperations([2,0,1,3]))  # -1
