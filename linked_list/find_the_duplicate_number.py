from __future__ import annotations


class Solution_:
    def findDuplicate(self, nums: List[int]) -> int:
        # naive O(n) space
        set_ = set()
        for n in nums:
            if n in set_:
                return n
            set_.add(n)

        return -1


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # good O(1) space, Floyd's (?) algo
        # len = n + 1, vals in [1, n]
        # ex. nums=[1,3,4,2,2] , len = 5, vals in [1, 4]
        # consider every value as a pointer (idx) to another position in list
        # detect a cycle, start of the cycle is the answer

        # Floyd's algo: init fast and slow pointer, slow moves one step at a time, fast - two
        # if there's a loop, they will meet
        slow = 0
        fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow_ = 0
        while slow_ != slow:
            slow = nums[slow]
            slow_ = nums[slow_]

        return slow



s = Solution()
print(s.findDuplicate([1,2,3,2,2]))
print(s.findDuplicate([1,2,3,4,4]))
