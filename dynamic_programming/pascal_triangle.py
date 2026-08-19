from __future__ import annotations
from time import perf_counter


class SolutionOrig:
    def generate(self, numRows: int) -> List[List[int]]:
        # there should be more readable solution lil bro
        def dfs(step, res, num):
            if step == num:
                return

            if step == 0:
                res.append([1])
                dfs(step + 1, res, num)
            elif step == 1:
                res.append([1, 1])
                dfs(step + 1, res, num)
            else:
                res.append([1])
                for i in range(len(res[step - 1]) - 1):
                    res[step].append(res[step - 1][i] + res[step - 1][i + 1])
                res[step].append(1)
                dfs(step + 1, res, num)

        res = []
        dfs(0, res, numRows)
        return res


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # there should be more readable solution lil bro
        def dfs(step, res, num):
            if step == num:
                return

            if step == 0:
                res.append([1])
                dfs(step + 1, res, num)
            elif step == 1:
                res.append([1, 1])
                dfs(step + 1, res, num)
            else:
                res.append([1])
                for i in range(len(res[step - 1]) - 1):
                    res[step].append(res[step - 1][i] + res[step - 1][i + 1])
                res[step].append(1)
                dfs(step + 1, res, num)

        res = []
        dfs(0, res, numRows)
        return res


class SolutionCleaner:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]

        prev_rows = self.generate(numRows - 1)
        new_row = [1] * numRows
        for i in range(1, len(prev_rows[-1])):
            new_row[i] = prev_rows[-1][i - 1] + prev_rows[-1][i]

        prev_rows.append(new_row)
        return prev_rows


# because recursive depth isn't infinite
class SolutionLoop:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]
        for i in range(numRows - 1):
            new_row = [1]
            for j in range(i):
                new_row.append(result[i][j] + result[i][j + 1])
            new_row.append(1)
            result.append(new_row)

        return result


if __name__ == "__main__":
    s = SolutionOrig()
    start = perf_counter()
    print(s.generate(5))  # [[1], [1,1], [1,2,1], [1,3,3,1], [1,4,6,4,1]]
    print(s.generate(1))  # [[1]]
    for _ in range(5): s.generate(700)
    sl = perf_counter() - start

    s = SolutionCleaner()
    start = perf_counter()
    print(s.generate(5))  # [[1], [1,1], [1,2,1], [1,3,3,1], [1,4,6,4,1]]
    print(s.generate(1))  # [[1]]
    for _ in range(5): s.generate(700)
    sf = perf_counter() - start

    s = SolutionLoop()
    start = perf_counter()
    print(s.generate(5))  # [[1], [1,1], [1,2,1], [1,3,3,1], [1,4,6,4,1]]
    print(s.generate(1))  # [[1]]
    for _ in range(5): s.generate(700)
    slp = perf_counter() - start
    print(f"Orig solution time: {sl:.2f}, alternative solution time: {sf:.2f}, loop solution time: {slp:.2f}")

