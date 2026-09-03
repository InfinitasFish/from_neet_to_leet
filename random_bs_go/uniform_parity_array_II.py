from __future__ import annotations


class SolutionOn2:
    def uniformArray(self, nums1: list[int]) -> bool:
        # hits time limit, not surprised because it's O(n^2)
        all_even = True
        all_odd = True

        # nums2[i] = nums1[i]
        # nums2[i] = nums1[i] - nums1[j], j != i, nums1[i] - nums1[j] >= 1
        for i in range(len(nums1)):
            if not all_even and not all_odd:
                break

            if nums1[i] % 2 == 0:
                found_odd = False
                for j in range(len(nums1)):
                    if i == j or nums1[i] - nums1[j] < 1:
                        continue
                    if (nums1[i] - nums1[j]) % 2 == 1:
                        found_odd = True
                        break
                if not found_odd:
                    all_odd = False

            else:
                found_even = False
                for j in range(len(nums1)):
                    if i == j or nums1[i] - nums1[j] < 1:
                        continue
                    if (nums1[i] - nums1[j]) % 2 == 0:
                        found_even = True
                        break
                if not found_even:
                    all_even = False

        return all_even or all_odd


class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        # similar idea to previous problem, but now we have additional rule nums1[i] - nums1[j] >= 1
        # to get around this we just can find the smallest odd number and the smallest even number,
        # if min_even - min_odd >= 1, we return true, because we can use this min_odd to turn all evens into odds
        # passes by time limit, but not the fastest solution
        odds = [n for n in nums1 if n % 2 == 1]
        if len(odds) == 0:
            return True

        evens = [n for n in nums1 if n % 2 == 0]
        if len(evens) == 0:
            return True

        return min(evens) - min(odds) >= 1


s = Solution()
print(s.uniformArray([1,4,7]))  # True
print(s.uniformArray([2,3]))  # False
print(s.uniformArray([4,6]))  # True

