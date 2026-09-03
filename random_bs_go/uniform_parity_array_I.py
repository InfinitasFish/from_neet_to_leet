from __future__ import annotations


class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        all_even = True
        all_odd = True

        # nums2[i] = nums1[i]
        # nums2[i] = nums1[i] - nums1[j], j != i
        for i in range(len(nums1)):
            if not all_even and not all_odd:
                break

            if nums1[i] % 2 == 0 and all_even:
                found_odd = False
                for j in range(len(nums1)):
                    if i == j:
                        continue
                    if nums1[i] - nums1[j] % 2 == 1:
                        found_odd = True
                        break
                if not found_odd:
                    all_odd = False

            elif all_odd:
                found_even = False
                for j in range(len(nums1)):
                    if i == j:
                        continue
                    if nums1[i] - nums1[j] % 2 == 0:
                        found_even = True
                        break
                if not found_even:
                    all_even = False

        return all_even or all_odd



s = Solution()
print(s.uniformArray([2,3]))  # True
print(s.uniformArray([4,6]))  # True

