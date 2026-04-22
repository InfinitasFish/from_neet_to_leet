from __future__ import annotations


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left_row = 0
        right_row = len(matrix) - 1
        found_target = False
        while left_row <= right_row:
            mid_row = (left_row + right_row) // 2

            if matrix[mid_row][0] <= target <= matrix[mid_row][-1]:
                # our target is in this row, if not - then no target in matrix
                left = 0
                right = len(matrix[mid_row]) - 1
                while left <= right:
                    mid = (left + right) // 2
                    if matrix[mid_row][mid] < target:
                        left = mid + 1
                    elif matrix[mid_row][mid] > target:
                        right = mid - 1
                    else:
                        found_target = True
                        break
                return found_target

            elif matrix[mid_row][0] > target:
                right_row = mid_row - 1
            else:
                left_row = mid_row + 1

        return found_target


print(Solution().searchMatrix([[1,2,4,8],[10,11,12,13],[14,20,30,40]], 15))
print(Solution().searchMatrix([[1,2,4,8],[10,11,12,13],[14,20,30,40]], 1))
print(Solution().searchMatrix([[1]], 2))
