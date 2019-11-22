#
# @lc app=leetcode id=829 lang=python3
#
# [829] Consecutive Numbers Sum
#
# https://leetcode.com/problems/consecutive-numbers-sum/description/
#
# algorithms
# Hard (34.29%)
# Likes:    218
# Dislikes: 323
# Total Accepted:    16K
# Total Submissions: 45.1K
# Testcase Example:  '5'
#
# Given a positive integer N, how many ways can we write it as a sum of
# consecutive positive integers?
# 
# Example 1:
# 
# 
# Input: 5
# Output: 2
# Explanation: 5 = 5 = 2 + 3
# 
# Example 2:
# 
# 
# Input: 9
# Output: 3
# Explanation: 9 = 9 = 4 + 5 = 2 + 3 + 4
# 
# Example 3:
# 
# 
# Input: 15
# Output: 4
# Explanation: 15 = 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5
# 
# Note: 1 <= N <= 10 ^ 9.
# 
#

# @lc code=start
class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        # ????based on ????
        # ?? ? i ? consecutive numnber ???? N
        # ? 1 + 2 + 3 + 4 + ... + i = i(i+1)/2
        #    2 + 3 + 4 + 5 + ... + i + i+1 = 1 + 2 + 3 + 4 + ... + i + i = i(i+1)/2 + i
        #    3 + 4 + 5 + 6 + ... + i + i+1 + i+2 = i(i+1)/2 + 2*i
        #    4 + 5 + 6 + 7 + ... + i + i+1 + i+2 + i+3 = i(i+1)/2 + 3*i
        # ?? N 
        if N == 1:
            return 1
        ret = 0
        for i in range(1,N):
            numerator = 2*N - i*(i+1)
            if numerator < 0:
                break
            if numerator % (2*i) == 0:
                ret += 1
        return ret
# @lc code=end

