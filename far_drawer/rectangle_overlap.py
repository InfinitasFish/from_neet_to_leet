from __future__ import annotations


class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        # easy problem
        # we want to reduce it to one dimension, take two intervals x1-x2 and x3-x4, for them to overlap
        # x1 < x4 and x3 < x2
        # for rectangle we will check this for vertical and horizontal vertices
        return rec1[0] < rec2[2] and rec2[0] < rec1[2] and rec1[1] < rec2[3] and rec2[1] < rec1[3]



s = Solution()
print(s.isRectangleOverlap([0,0,2,2], [1,1,3,3]))  # True
print(s.isRectangleOverlap([0,0,1,1], [2,2,3,3]))  # False
print(s.isRectangleOverlap([0,0,1,1], [1,0,2,1]))  # False
print(s.isRectangleOverlap([2,17,6,20], [3,8,6,20]))  # True

