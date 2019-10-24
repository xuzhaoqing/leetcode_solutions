#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#
# https://leetcode.com/problems/unique-paths/description/
#
# algorithms
# Medium (49.19%)
# Likes:    1986
# Dislikes: 144
# Total Accepted:    345.7K
# Total Submissions: 695.6K
# Testcase Example:  '3\n2'
#
# A robot is located at the top-left corner of a m x n grid (marked 'Start' in
# the diagram below).
# 
# The robot can only move either down or right at any point in time. The robot
# is trying to reach the bottom-right corner of the grid (marked 'Finish' in
# the diagram below).
# 
# How many possible unique paths are there?
# 
# 
# Above is a 7 x 3 grid. How many possible unique paths are there?
# 
# Note: m and n will be at most 100.
# 
# Example 1:
# 
# 
# Input: m = 3, n = 2
# Output: 3
# Explanation:
# From the top-left corner, there are a total of 3 ways to reach the
# bottom-right corner:
# 1. Right -> Right -> Down
# 2. Right -> Down -> Right
# 3. Down -> Right -> Right
# 
# 
# Example 2:
# 
# 
# Input: m = 7, n = 3
# Output: 28
# 
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m <= 0 or n <= 0:
            return 0

        dp = [[0 for _ in range(n)] for _ in range(m)]

        for row in range(m):
            for col in range(n):
                if row == 0 or col == 0:
                    dp[row][col] = 1
                else:
                    dp[row][col] = dp[row-1][col] + dp[row][col-1]

        return dp[m-1][n-1]
        
# @lc code=end

