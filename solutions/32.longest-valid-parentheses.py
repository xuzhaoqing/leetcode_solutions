#
# @lc app=leetcode id=32 lang=python3
#
# [32] Longest Valid Parentheses
#
# https://leetcode.com/problems/longest-valid-parentheses/description/
#
# algorithms
# Hard (26.33%)
# Likes:    2393
# Dislikes: 109
# Total Accepted:    223.5K
# Total Submissions: 841.6K
# Testcase Example:  '"(()"'
#
# Given a string containing just the characters '(' and ')', find the length of
# the longest valid (well-formed) parentheses substring.
# 
# Example 1:
# 
# 
# Input: "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()"
# 
# 
# Example 2:
# 
# 
# Input: ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()"
# 
# 
#

# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        longestValidPar = 0
        currValidPar = 0
        for i,par in enumerate(s):
            if par == '(':
                stack.append(i)
            else:
                if stack:
                    stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    longestValidPar = max(longestValidPar, i-stack[-1])
        
        return longestValidPar
        
# @lc code=end

