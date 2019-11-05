#
# @lc app=leetcode id=647 lang=python3
#
# [647] Palindromic Substrings
#
# https://leetcode.com/problems/palindromic-substrings/description/
#
# algorithms
# Medium (57.95%)
# Likes:    1739
# Dislikes: 87
# Total Accepted:    129K
# Total Submissions: 221.2K
# Testcase Example:  '"abc"'
#
# Given a string, your task is to count how many palindromic substrings in this
# string.
# 
# The substrings with different start indexes or end indexes are counted as
# different substrings even they consist of same characters.
# 
# Example 1:
# 
# 
# Input: "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".
# 
# 
# 
# 
# Example 2:
# 
# 
# Input: "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
# 
# 
# 
# 
# Note:
# 
# 
# The input string length won't exceed 1000.
# 
# 
# 
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        N = len(s)
        dp = [[False] * N for _ in range(N)]
        count = 0
        for end in range(N):
            for start in range(end+1):
                if s[start] == s[end] and (end - start < 2 or dp[start+1][end-1]):
                    dp[start][end] = True
                    count += 1
        return count
# @lc code=end

