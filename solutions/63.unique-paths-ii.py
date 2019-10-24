#
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#
# https://leetcode.com/problems/unique-paths-ii/description/
#
# algorithms
# Medium (33.69%)
# Likes:    1058
# Dislikes: 175
# Total Accepted:    232.1K
# Total Submissions: 688.1K
# Testcase Example:  '[[0,0,0],[0,1,0],[0,0,0]]'
#
# A robot is located at the top-left corner of a m x n grid (marked 'Start' in
# the diagram below).
# 
# The robot can only move either down or right at any point in time. The robot
# is trying to reach the bottom-right corner of the grid (marked 'Finish' in
# the diagram below).
# 
# Now consider if some obstacles are added to the grids. How many unique paths
# would there be?
# 
# 
# 
# An obstacle and empty space is marked as 1 and 0 respectively in the grid.
# 
# Note: m and n will be at most 100.
# 
# Example 1:
# 
# 
# Input:
# [
# [0,0,0],
# [0,1,0],
# [0,0,0]
# ]
# Output: 2
# Explanation:
# There is one obstacle in the middle of the 3x3 grid above.
# There are two ways to reach the bottom-right corner:
# 1. Right -> Right -> Down -> Down
# 2. Down -> Down -> Right -> Right
# 
# 
#

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid:
            return 0

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [[0 for _ in range(n)] for _ in range(m)]

        for row in range(m):
            for col in range(n):
                if row == 0 or col == 0:
                    dp[row][col] = 1
                elif obstacleGrid[row][col] == 1:
                    dp[row][col] = 0
                else:
                    dp[row][col] = dp[row-1][col] + dp[row][col-1]

        return dp[m-1][n-1]

# @lc code=end

