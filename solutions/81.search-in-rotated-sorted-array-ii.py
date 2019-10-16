# -*- coding: utf-8 -*-

# @lc app=leetcode id=81 lang=python3
#
# [81] Search in Rotated Sorted Array II
#
# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/
#
# algorithms
# Medium (32.75%)
# Likes:    827
# Dislikes: 359
# Total Accepted:    192.8K
# Total Submissions: 588K
# Testcase Example:  '[2,5,6,0,0,1,2]\n0'
#
# Suppose an array sorted in ascending order is rotated at some pivot unknown
# to you beforehand.
# 
# (i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).
# 
# You are given a target value to search. If found in the array return true,
# otherwise return false.
# 
# Example 1:
# 
# 
# Input: nums = [2,5,6,0,0,1,2], target = 0
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: nums = [2,5,6,0,0,1,2], target = 3
# Output: false
# 
# Follow up:
# 
# 
# This is a follow up problem to Search in Rotated Sorted Array, where nums may
# contain duplicates.
# Would this affect the run-time complexity? How and why?
# 
# 
#

# @lc code=start
class Solution:
    def search(self, nums, target) -> bool:
        N = len(nums)
        low, high = 0, N-1
        while low <= high:
            while low < high and nums[low] == nums[high]:
                low += 1
            
            mid = (low + high) >> 1
            if nums[mid] == target:
                return True
            elif nums[mid] >= nums[low]: # high section
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else: # low section
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return False


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    nums =  [5,1,3]

    target = 3
    print(s.search(nums,target))
