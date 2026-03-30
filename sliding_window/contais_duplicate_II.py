from __future__ import annotations


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        vals = set()
        left = 0
        for right in range(len(nums)):
            if right - left > k:
                vals.remove(nums[left])
                left += 1

            if nums[right] in vals:
                return True

            vals.add(nums[right])

        return False

print(Solution().containsNearbyDuplicate([1,2,3,1], 3))  # True
print(Solution().containsNearbyDuplicate([1,2,3,1], 2))  # False
print(Solution().containsNearbyDuplicate([1,2,3,4,5,6,6,6], 2))  # True
print(Solution().containsNearbyDuplicate([2,1,2], 1))  # False
print(Solution().containsNearbyDuplicate([0,1,2,3,2,5], 3))  # True
print(Solution().containsNearbyDuplicate([1,4,2,3,1,2], 3))  # True
