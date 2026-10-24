from __future__ import annotations


class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        months_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        a_start = sum([months_days[i] for i in range(int(arriveAlice[:2]) - 1)]) + int(arriveAlice[3:])
        a_end = sum([months_days[i] for i in range(int(leaveAlice[:2]) - 1)]) + int(leaveAlice[3:])

        b_start = sum([months_days[i] for i in range(int(arriveBob[:2]) - 1)]) + int(arriveBob[3:])
        b_end = sum([months_days[i] for i in range(int(leaveBob[:2]) - 1)]) + int(leaveBob[3:])

        if a_end < b_start and b_end > a_start or b_end < a_start and a_end > b_start:
            return 0

        if a_start <= b_start and a_end >= b_end:
            return b_end - b_start + 1

        if b_start <= a_start and b_end >= a_end:
            return a_end - a_start + 1

        if b_start <= a_end <= b_end:
            return a_end - b_start + 1
        else:
            return b_end - a_start + 1

        # actual formula to check intersection: min(a_end, b_end) - max(a_start, b_start)


s = Solution()
print(s.countDaysTogether("08-15", "08-18","08-16", "08-19"))  # 3
print(s.countDaysTogether("10-01", "10-31", "11-01", "12-31"))  # 0
print(s.countDaysTogether("08-06", "12-08", "02-04", "09-01"))  # 27
