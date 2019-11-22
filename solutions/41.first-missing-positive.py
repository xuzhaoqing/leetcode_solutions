#
# @lc app=leetcode id=41 lang=python3
#
# [41] First Missing Positive
#
# https://leetcode.com/problems/first-missing-positive/description/
#
# algorithms
# Hard (29.74%)
# Likes:    2174
# Dislikes: 653
# Total Accepted:    250.5K
# Total Submissions: 836.2K
# Testcase Example:  '[1,2,0]'
#
# Given an unsorted integer array, find the smallest missing positive integer.
# 
# Example 1:
# 
# 
# Input: [1,2,0]
# Output: 3
# 
# 
# Example 2:
# 
# 
# Input: [3,4,-1,1]
# Output: 2
# 
# 
# Example 3:
# 
# 
# Input: [7,8,9,11,12]
# Output: 1
# 
# 
# Note:
# 
# Your algorithm should run in O(n) time and uses constant extra space.
# 
#

# @lc code=start
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        N = len(nums)
        has_num = [False] * N

        for n in nums:
            if 0 < n < N+1:
                has_num[n-1] = True
        
        for i in range(N):
            if not has_num[i]:
                return i+1
        return N + 1





# @lc code=end

