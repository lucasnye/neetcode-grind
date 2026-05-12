class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Go to middle row and find the left and right value
        n_rows = len(matrix)
        mid = n_rows // 2
        mid_row = matrix[mid]
        n_columns = len(mid_row)
        left = 0
        right = n_columns - 1
        # If target >= left AND target <= right:
        if target >= mid_row[left] and target <= mid_row[right]:
            # Perform binary search on the row
            result = self.bs_recursive(left, right, mid_row, target)

        # Elif target < left
        elif target < mid_row[left]:
            # While target < left:
            target_row = mid
            while target < matrix[target_row][left]:
                # Go up one row
                target_row -= 1
                if target_row < 0:
                    return False
            # Perform binary search on the row
            result = self.bs_recursive(left, right, matrix[target_row], target)

        # Elif target > right:
        # elif target > mid_row[right]:
        else:
            target_row = mid
            # While target > right:
            while target > matrix[target_row][right]:
                # Go down one row
                target_row += 1
                if target_row > n_rows - 1:
                    return False
            # Perform binary search on the row
            result = self.bs_recursive(left, right, matrix[target_row], target)

        return False if result == -1 else True
    
    def bs_recursive(self, l: int, r: int, nums: List[int], target: int) -> int:
        if l > r:
            return -1
        m = l + (r - l) // 2
        if nums[m] == target:
            return m
        elif nums[m] < target:
            return self.bs_recursive(m + 1, r, nums, target)
        else:
            return self.bs_recursive(l, m - 1, nums, target)