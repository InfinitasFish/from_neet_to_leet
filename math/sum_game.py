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

        # no question marks => compare sums
        if right_qm + left_qm == 0:
            return not right_sum == left_sum

        # odd number of question marks => alice always wins by tipping on last step
        if (right_qm + left_qm) % 2 == 1:
            return True

        # winner will depend only on unpaired question marks and sums difference,
        # other question marks will cancel out

        # also for Bob to have a chance, the side that's ahead in sum must be the side with fewer ? marks
        # if sign of these is different, it means that alice can tip the leading sum and bob won't be able to fill
        # the difference
        diff_qm = right_qm - left_qm
        diff_sum = left_sum - right_sum

        # even number of question marks => bob only wins when the difference is divisible
        # by 9 and there's enough marks to close difference out (+9 for each pair)
        # so bob wins when diff_qm // 2 * 9 == diff_sum
        # if diff_sum is smaller, alice will 'overflow' it, if bigger, alice will place zeros
        # and bob won't have enough nines to fill difference
        if diff_qm // 2 * 9 == diff_sum:
            return False
        else:
            return True


if __name__ == "__main__":
    s = Solution()
    # print(s.sumGame("5023"))  # False
    # print(s.sumGame("25??"))  # True
    # print(s.sumGame("?3295???"))  # False
    # print(s.sumGame("9?"))  # True
    print(s.sumGame("?6?6?000?3"))  # True
