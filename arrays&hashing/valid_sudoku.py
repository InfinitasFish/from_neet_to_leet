from __future__ import annotations
from collections import defaultdict


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # naive N*N + N*N + N*N -> O(N^2), but N=9, so it's kinda 3*9*9 -> O(1)
        # better do all checks in one cycle
        cols_map = defaultdict(list)
        rows_map = defaultdict(list)
        squares_map = defaultdict(list)
        for i in range(len(board)):
            for j in range(i, len(board[i])):
                if board[i][j] != '.':
                    square_idx_key = f'{i // 3}{j // 3}'
                    if board[i][j] not in squares_map[square_idx_key]:
                        squares_map[square_idx_key].append(board[i][j])
                    else:
                        return False

                    if board[i][j] not in rows_map[i]:
                        rows_map[i].append(board[i][j])
                    else:
                        return False

                    if board[i][j] not in cols_map[j]:
                        cols_map[j].append(board[i][j])
                    else:
                        return False

                if board[j][i] != '.' and i != j:
                    square_idx_key = f'{j // 3}{i // 3}'
                    if board[j][i] not in squares_map[square_idx_key]:
                        squares_map[square_idx_key].append(board[j][i])
                    else:
                        return False

                    if board[j][i] not in rows_map[j]:
                        rows_map[j].append(board[j][i])
                    else:
                        return False

                    if board[j][i] not in cols_map[i]:
                        cols_map[i].append(board[j][i])
                    else:
                        return False

        return True

board = [["1","2",".",".","3",".",".",".","."],
         ["4",".",".","5",".",".",".",".","."],
         [".","9","1",".",".",".",".",".","3"],
         ["5",".",".",".","6",".",".",".","4"],
         [".",".",".","8",".","3",".",".","5"],
         ["7",".",".",".","2",".",".",".","6"],
         [".",".",".",".",".",".","2",".","."],
         [".",".",".","4","1","9",".",".","8"],
         [".",".",".",".","8",".",".","7","9"]]
print(Solution().isValidSudoku(board))
