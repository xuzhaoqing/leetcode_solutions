#
# @lc app=leetcode id=718 lang=python3
#
# [718] Maximum Length of Repeated Subarray
#
# https://leetcode.com/problems/maximum-length-of-repeated-subarray/description/
#
# algorithms
# Medium (47.32%)
# Likes:    806
# Dislikes: 34
# Total Accepted:    43.6K
# Total Submissions: 91.4K
# Testcase Example:  '[1,2,3,2,1]\n[3,2,1,4,7]'
#
# Given two integer arrays A and B, return the maximum length of an subarray
# that appears in both arrays.
# 
# Example 1:
# 
# 
# Input:
# A: [1,2,3,2,1]
# B: [3,2,1,4,7]
# Output: 3
# Explanation: 
# The repeated subarray with maximum length is [3, 2, 1].
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= len(A), len(B) <= 1000
# 0 <= A[i], B[i] < 100
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        lenA, lenB = len(A), len(B)
        
        dp = [[0 for _ in range(lenB+1)] for _ in range(lenA+1)]
        
        for i in range(lenA-1,-1,-1):
            for j in range(lenB-1, -1, -1):
                if A[i] == B[j]:
                    dp[i][j] = dp[i+1][j+1] + 1
        return max(max(row) for row in dp)
    
# @lc code=end

