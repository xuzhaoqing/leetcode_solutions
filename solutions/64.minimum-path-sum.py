#
# @lc app=leetcode id=64 lang=python3
#
# [64] Minimum Path Sum
#
# https://leetcode.com/problems/minimum-path-sum/description/
#
# algorithms
# Medium (48.65%)
# Likes:    1704
# Dislikes: 44
# Total Accepted:    270.9K
# Total Submissions: 551.5K
# Testcase Example:  '[[1,3,1],[1,5,1],[4,2,1]]'
#
# Given a m x n grid filled with non-negative numbers, find a path from top
# left to bottom right which minimizes the sum of all numbers along its path.
# 
# Note: You can only move either down or right at any point in time.
# 
# Example:
# 
# 
# Input:
# [
# [1,3,1],
# ⁠ [1,5,1],
# ⁠ [4,2,1]
# ]
# Output: 7
# Explanation: Because the path 1→3→1→1→1 minimizes the sum.
# 
# 
#

# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        
        dp = [[0 for _ in range(n)] for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]
                elif j == 0:
                    dp[i][j] = dp[i-1][j] + grid[i][j]
                elif i == 0:
                    dp[i][j] = dp[i][j-1] + grid[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
                    
        return dp[m-1][n-1]
# @lc code=end

