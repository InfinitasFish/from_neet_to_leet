from __future__ import annotations
from time import perf_counter


BIG = big = [-1,-69,544,-440,-622,-967,-61,-249,757,158,953,813,360,301,542,26,-500,-228,-693,705,-485,-734,-484,349,-211,-508,-555,-512,936,-959,-424,-577,-659,854,-968,876,-619,-658,328,-303,101,96,949,-980,-995,863,629,-823,-459,-57,994,-203,-787,-828,290,2,164,-539,-9,-446,622,140,18,282,-96,-3,829,896,-829,767,522,-712,-527,-795,656,-242,822,-984,543,-576,-318,-379,-987,252,-727,98,-909,-238,814,-159,-245,322,-861,-16,-562,31,418,378,396,893,-94,-226,84,-896,627,-953,840,-164,915,-632,-540,-213,702,208,152,513,804,-127,121,279,651,-80,-838,-927,887,-853,128,869,7,-703,220,-924,-583,-943,-206,485,-819,245,-835,442,-543,-986,533,696,-716,-650,-774,175,358,-803,102,-116,-535,-678,950,855,-615,167,962,-415,897,694,-723,-731,174,-376,751,165,-958,838,616,877,-715,-707,634,-589,-316,60,-697,839,413,-845,564,333,-514,986,998,-673,475,-836,-334,460,-826,649,185,868,-834,-554,235,148,-511,810,155,948,906,910,-85,769,-815,826,-248,-425,-110,137,78,127,-824,-932,82,264,-890,-377,205,249,-954,241,958,30,508,-719,35,-662,254,-930,186,761,-277,537,-471,-348,-750,766,899,-843,604,960,455,786,19,-151,172,401,652,-271,131,551,115,911,-223,912,408,296,364,-117,623,-616,-204,162,-946,207,81,-590,315,4,-692,985,-919,332,395,426,898,529,240,-799,-637,-801,-830,-407,409,-735,-918,816,502,-797,-949,938,118,-768,389,-886,-220,181,-760,-464,-911,519,-39,5,515,-602,132,-818,-625,-878,977,647,269,732,825,126,-480,170,-738,-591,716]

# my first solution
class SolutionSlow:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        def twoSumClosest(nums, target) -> Tuple[int]:
            map = {k: i for i, k in enumerate(nums)}
            min_dist = float("inf")
            l = -1
            r = -1
            for i, n in enumerate(nums):
                second = target - n
                if second in map and map[second] != i:
                    return i, map[second]
                # this part is slow, basically O(n) to find element that gives minimal distance
                # in case we don't have perfect match (so most cases)
                # in the worst case with two addition outer cycles, we get O(n^3)
                elif i + 1 < len(nums):
                    dist_map = {k: abs(second - k) for k in nums[i + 1:]}
                    best_third = min(dist_map.items(), key=lambda x: x[1])[0]
                    dist = abs(target - (best_third + n))
                    if dist < min_dist:
                        min_dist = dist
                        l = i
                        r = map[best_third]

            return l, r

        min_dist = float("inf")
        best_sum = -1
        for i, n in enumerate(nums):
            two_sum_target = target - n
            second, third = twoSumClosest(nums[i + 1:], two_sum_target)
            if second == -1 or third == -1:
                continue

            # proper offset to align with full nums
            second += i + 1
            third += i + 1

            three_sum = n + nums[second] + nums[third]
            dist = abs(target - three_sum)
            if dist == 0:
                return three_sum

            if dist < min_dist:
                min_dist = dist
                best_sum = three_sum

        return best_sum


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # faster version just utilizes sort and applies two pointers
        # basically we will have O(n*log(n) + n^2) = O(n^2) time complexity instead of O(n^3)
        nums = sorted(nums)
        result = nums[0] + nums[1] + nums[2]
        n = len(nums)
        for i in range(n - 2):
            l = i + 1
            r = n - 1
            while l < r:
                new_result = nums[i] + nums[l] + nums[r]
                if new_result == target:
                    return new_result

                if abs(target - new_result) < abs(target - result):
                    result = new_result
                if new_result < target:
                    l += 1
                else:
                    r -= 1

        return result


if __name__ == "__main__":
    sl = SolutionSlow()
    sf = Solution()
    print(sf.threeSumClosest([-1, 2, 1, -4], 1))  # 2
    print(sf.threeSumClosest([0, 0, 0], 1))  # 0
    print(sf.threeSumClosest([1, 1, 1, 0], -100))  # 2
    print(sf.threeSumClosest([1, 2, 7, 13], 12))

    start = perf_counter()
    print(sl.threeSumClosest(BIG,6539))  # 2978
    slow_time = perf_counter() - start
    start = perf_counter()
    print(sf.threeSumClosest(BIG, 6539))  # 2978
    fast_time = perf_counter() - start
    print(f"Slower solution time: {slow_time:.2f}\nFaster solution time: {fast_time:.2f}")

