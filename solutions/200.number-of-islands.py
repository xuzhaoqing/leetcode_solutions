#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#
# https://leetcode.com/problems/number-of-islands/description/
#
# algorithms
# Medium (42.88%)
# Likes:    3512
# Dislikes: 129
# Total Accepted:    474.5K
# Total Submissions: 1.1M
# Testcase Example:  '[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]'
#
# Given a 2d grid map of '1's (land) and '0's (water), count the number of
# islands. An island is surrounded by water and is formed by connecting
# adjacent lands horizontally or vertically. You may assume all four edges of
# the grid are all surrounded by water.
# 
# Example 1:
# 
# 
# Input:
# 11110
# 11010
# 11000
# 00000
# 
# Output: 1
# 
# 
# Example 2:
# 
# 
# Input:
# 11000
# 11000
# 00100
# 00011
# 
# Output: 3
# 
#

# @lc code=start
from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        def dfs(x,y):
            if grid[x][y] == '1' and (x,y) not in visited:
                visited.add((x,y))
            else:
                return
            if x > 0:
                dfs(x-1,y)
            if x < len(grid)-1:
                dfs(x+1,y)
            if y > 0:
                dfs(x,y-1)
            if y < len(grid[0]) - 1:
                dfs(x,y+1)
        
        counter = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and (i,j) not in visited:
                    dfs(i,j)
                    counter += 1
        
        return counter
# @lc code=end

