#
# @lc app=leetcode id=214 lang=python3
#
# [214] Shortest Palindrome
#
# https://leetcode.com/problems/shortest-palindrome/description/
#
# algorithms
# Hard (28.18%)
# Likes:    796
# Dislikes: 92
# Total Accepted:    83.3K
# Total Submissions: 293.6K
# Testcase Example:  '"aacecaaa"'
#
# Given a string s, you are allowed to convert it to a palindrome by adding
# characters in front of it. Find and return the shortest palindrome you can
# find by performing this transformation.
# 
# Example 1:
# 
# 
# Input: "aacecaaa"
# Output: "aaacecaaa"
# 
# 
# Example 2:
# 
# 
# Input: "abcd"
# Output: "dcbabcd"
#

# @lc code=start
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return ''
        for i in range(len(s),0,-1):
            if s[:i][::-1] == s[:i]:
                return s[i:][::-1] + s
# @lc code=end

