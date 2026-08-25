from __future__ import annotations


class Solution:
    def sumGame(self, num: str) -> bool:
        # we need some kind of greedy algo, for example first player will be trying
        # to maximize difference between two sums, and second will try to minimize it

        # upd. my idea doesn't work entirely because the game conclusion depends on not only
        # sums difference, but whether amount of '?' is even or odd
        # to simplify the state, first we eliminate paired question marks from both sides (bob can cancel them out)
        # then we will have three cases: no question marks, odd question marks on one side, even question marks on one side
        # then we calculate whether bob can close out difference between sums on his turns
        left_sum = 0
        left_qm = 0
        right_qm = 0
        right_sum = 0
        mid = len(num) // 2 - 1
        for i in range(mid + 1):
            if num[i] == '?':
                left_qm += 1
            else:
                left_sum += int(num[i])

        for i in range(mid + 1, len(num)):
            if num[i] == '?':
                right_qm += 1
            else:
                right_sum += int(num[i])

        if right_qm + left_qm == 0:
            return not right_sum == left_sum

        diff_qm = abs(left_qm - right_qm)
        diff_sum = abs(right_sum)
        # each pair can subtract 9 from difference
        pairs = diff_qm // 2







if __name__ == "__main__":
    s = Solution()
    print(s.sumGame("5023"))  # False
    print(s.sumGame("25??"))  # True
    print(s.sumGame("?3295???"))  # False
    print(s.sumGame("9?"))  # True
