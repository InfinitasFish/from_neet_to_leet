from __future__ import annotations
import heapq


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # the first idea that comes to mind is to use max-heap
        # and this time first idea works perfectly
        if k >= len(nums):
            return [max(nums)]

        # trick to make max-heap out of min-heap
        heap = [(-nums[i], i) for i in range(k)]
        heapq.heapify(heap)

        result = [-heap[0][0]]
        for r in range(k, len(nums)):
            heapq.heappush(heap, (-nums[r], r))

            while heap[0][1] < r - k + 1:
                heapq.heappop(heap)

            result.append(-heap[0][0])
        return result


s = Solution()
print(s.maxSlidingWindow([1,2,1,0,4,2,6], 3))  # [2,2,4,4,6]
print(s.maxSlidingWindow([1,1,1,2,2,2,3,3,3,10], 4))  # [2,2,2,3,3,3,10]
print(s.maxSlidingWindow([1,3,1,2,0,5], 3))  # [3,3,2,5]
print(s.maxSlidingWindow([9,10,9,-7,-4,-8,2,-6], 5))  # [10,10,9,2]
