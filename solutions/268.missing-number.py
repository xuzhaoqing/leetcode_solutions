#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#
# https://leetcode.com/problems/missing-number/description/
#
# algorithms
# Easy (49.25%)
# Likes:    1169
# Dislikes: 1590
# Total Accepted:    342.6K
# Total Submissions: 690.6K
# Testcase Example:  '[3,0,1]'
#
# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find
# the one that is missing from the array.
# 
# Example 1:
# 
# 
# Input: [3,0,1]
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: [9,6,4,2,3,5,7,0,1]
# Output: 8
# 
# 
# Note:
# Your algorithm should run in linear runtime complexity. Could you implement
# it using only constant extra space complexity?
#

# @lc code=start
class Solution:
    def missingNumber(self, s: List[int]) -> int:
        if not s:
            return 0

        s.sort()
        if s[-1] == len(s)-1:
            return len(s)

        low, high = 0, len(s)-1
        while low < high:
            mid = (low + high) >> 1
            if s[mid] == mid:
                low = mid + 1
            else:
                high = mid

        return s[low]-1        
# @lc code=end

