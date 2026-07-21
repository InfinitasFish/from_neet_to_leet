from __future__ import annotations


class SolutionSlow:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # target O(log(m+n))
        m = len(nums1)
        n = len(nums2)
        l1 = 0
        l2 = 0
        join = []
        while l1 < m and l2 < n:
            if nums1[l1] <= nums2[l2]:
                join.append(nums1[l1])
                l1 += 1
            else:
                join.append(nums2[l2])
                l2 += 1

        while l1 < m:
            join.append(nums1[l1])
            l1 += 1

        while l2 < n:
            join.append(nums2[l2])
            l2 += 1

        if len(join) % 2 == 0:
            return float( (join[len(join)//2] + join[len(join)//2 - 1]) / 2)
        else:
            return float(join[len(join)//2])


class Solution:
    # the idea is to simulate partitions (left and right) of joined array without joining it
    # [1,2,3,4,5,6,7,8] [1,2,3,4]
    # joined [1,1,2,2,3,3,4,4,5,5,6,7,8]
    # total = 12, half = 6 for each partition
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # target O(log(m+n))

        # find shorter array to align partitions
        if len(nums1) < len(nums2):
            short_nums = nums1
            long_nums = nums2
        else:
            short_nums = nums2
            long_nums = nums1

        def findMedian(short_nums: List[int], long_nums: List[int]) -> float:

            total = len(short_nums) + len(long_nums)
            half = total // 2
            l = 0
            r = len(short_nums) - 1

            # search target is basically correct slice of shorter array that corresponds to left partition
            # of joined array
            ALeft, BLeft, ARight, BRight = 0, 0, 0, 0
            while True:
                AMid = l + (r - l) // 2
                BMid = half - AMid - 2

                # in correct left partition right-most element should be <=
                # than first element in right partition
                ALeft = short_nums[AMid] if AMid >= 0 else -float("inf")
                ARight = short_nums[AMid + 1] if (AMid + 1) < len(short_nums) else float("inf")
                BLeft = long_nums[BMid] if BMid >= 0 else -float("inf")
                BRight = long_nums[BMid + 1] if (BMid + 1) < len(long_nums) else float("inf")

                if ALeft <= BRight and BLeft <= ARight:
                    if total % 2 == 0:
                        return float((max(ALeft, BLeft) + min(ARight, BRight)) / 2)
                    else:
                        return float(min(ARight, BRight))
                elif ALeft > BRight:
                    r = AMid - 1
                else:
                    l = AMid + 1

        return findMedian(short_nums, long_nums)


if __name__ == "__main__":
    s = Solution()
    print(s.findMedianSortedArrays([1, 2], [3]))  # 2.0
    print(s.findMedianSortedArrays([1, 2, 3], [4, 5, 6, 7]))  # 4.0
    print(s.findMedianSortedArrays([1, 3], [2, 4]))  # 2.5
    print(s.findMedianSortedArrays([1,2,3,4,5,6,7,8], [1,2,3,4]))  # 3.5
