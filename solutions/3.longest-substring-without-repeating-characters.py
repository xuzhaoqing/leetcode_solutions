#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (28.86%)
# Likes:    6703
# Dislikes: 394
# Total Accepted:    1.2M
# Total Submissions: 4M
# Testcase Example:  '"abcabcbb"'
#
# Given a string, find the length of the longest substring without repeating
# characters.
# 
# 
# Example 1:
# 
# 
# Input: "abcabcbb"
# Output: 3 
# Explanation: The answer is "abc", with the length of 3. 
# 
# 
# 
# Example 2:
# 
# 
# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# 
# 
# 
# Example 3:
# 
# 
# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3. 
# ⁠            Note that the answer must be a substring, "pwke" is a
# subsequence and not a substring.
# 
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = ''
        longest = 0
        for char in s:
            if char not in substring:
                substring += char
            else:
                longest = max(longest, len(substring))
                substring = substring.split(char)[-1] + char
        
        longest = max(longest,len(substring))
        return longest
# @lc code=end

