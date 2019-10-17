#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
#
# algorithms
# Medium (34.23%)
# Likes:    2098
# Dislikes: 99
# Total Accepted:    362.9K
# Total Submissions: 1.1M
# Testcase Example:  '[5,7,7,8,8,10]\n8'
#
# Given an array of integers nums sorted in ascending order, find the starting
# and ending position of a given target value.
# 
# Your algorithm's runtime complexity must be in the order of O(log n).
# 
# If the target is not found in the array, return [-1, -1].
# 
# Example 1:
# 
# 
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# 
# Example 2:
# 
# 
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# 
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        N = len(nums)
        low,high = 0, N-1
        while low <= high:
            mid = (low+high) >> 1
            if nums[mid] == target:
                p = mid-1
                while p >= low and nums[p] == nums[mid]:
                    p -= 1
                low,p = p + 1, mid+1
                while p <= high and nums[p] == nums[mid]:
                    p += 1
                high = p-1
                return [low,high]
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return [-1,-1]
        
# @lc code=end

