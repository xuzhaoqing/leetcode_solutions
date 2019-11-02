#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#
# https://leetcode.com/problems/search-a-2d-matrix/description/
#
# algorithms
# Medium (35.24%)
# Likes:    1093
# Dislikes: 127
# Total Accepted:    259.4K
# Total Submissions: 731.9K
# Testcase Example:  '[[1,3,5,7],[10,11,16,20],[23,30,34,50]]\n3'
#
# Write an efficient algorithm that searches for a value in an m x n matrix.
# This matrix has the following properties:
# 
# 
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the
# previous row.
# 
# 
# Example 1:
# 
# 
# Input:
# matrix = [
# ⁠ [1,   3,  5,  7],
# ⁠ [10, 11, 16, 20],
# ⁠ [23, 30, 34, 50]
# ]
# target = 3
# Output: true
# 
# 
# Example 2:
# 
# 
# Input:
# matrix = [
# ⁠ [1,   3,  5,  7],
# ⁠ [10, 11, 16, 20],
# ⁠ [23, 30, 34, 50]
# ]
# target = 13
# Output: false
# 
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        
        M,N = len(matrix), len(matrix[0])
        if M == 1 and N == 1:
            return matrix[0][0] == target
        
        low_row, high_row = 0, M-1
        
        while low_row <= high_row:
            mid = (low_row + high_row) >> 1
            if matrix[mid][0] <= target and matrix[mid][N-1] >= target:
                low_row = mid 
                break
            elif matrix[mid][0] < target:
                low_row = mid + 1
            else:
                high_row = mid - 1
        
        if low_row >= M:
            return False 
        
        low_col, high_col = 0, N-1
        while low_col <= high_col:
            mid = (low_col + high_col) >> 1
            if matrix[low_row][mid] < target:
                low_col = mid + 1
            elif matrix[low_row][mid] > target:
                high_col = mid - 1
            else:
                return True
        
        return False
# @lc code=end

