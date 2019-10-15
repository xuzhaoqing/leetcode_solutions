#
# @lc app=leetcode id=264 lang=python3
#
# [264] Ugly Number II
#
# https://leetcode.com/problems/ugly-number-ii/description/
#
# algorithms
# Medium (37.45%)
# Likes:    1092
# Dislikes: 73
# Total Accepted:    115.6K
# Total Submissions: 308.5K
# Testcase Example:  '10'
#
# Write a program to find the n-th ugly number.
# 
# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 
# 
# Example:
# 
# 
# Input: n = 10
# Output: 12
# Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10
# ugly numbers.
# 
# Note:  
# 
# 
# 1 is typically treated as an ugly number.
# n does not exceed 1690.
# 
#
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n == 1:
            return 1
        
        dp = [1] * n
        u2, u3, u5 = 0,0,0
        
        for i in range(1,n):
            min_value = min(dp[u2]*2, dp[u3]*3,dp[u5]*5)
            if min_value == dp[u2]*2:
                u2 += 1
            if min_value == dp[u3]*3:
                u3 += 1
            if min_value == dp[u5]*5:
                u5 += 1
            
            dp[i] = min_value
        return dp[n-1]

