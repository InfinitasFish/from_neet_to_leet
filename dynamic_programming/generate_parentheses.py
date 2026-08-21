from __future__ import annotations


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # the idea is to add left parenthesis until we hit n, and add right ones accordingly
        # we will have two branches:
        # first just adds '(', and second adds ')' if we have enough left parenthesis
        # we will add the combination to the result if it has n * 2 characters
        # and then stop recursion
        def dfs(left, right, comb, n, res):
            if len(comb) == n * 2:
                res.append(comb)

            if left < n:
                dfs(left + 1, right, comb + '(', n, res)
            if right < left:
                dfs(left, right + 1, comb + ')', n, res)

        res = []
        dfs(0, 0, '', n, res)
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.generateParenthesis(3))  # ["((()))","(()())","(())()","()(())","()()()"]
    print(s.generateParenthesis(1))  # ["()"]

    texp = sorted(["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"])
    res = sorted(s.generateParenthesis(4))
    print(texp)
    print(res)
