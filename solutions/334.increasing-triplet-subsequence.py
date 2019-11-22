#
# @lc app=leetcode id=334 lang=python3
#
# [334] Increasing Triplet Subsequence
#
# https://leetcode.com/problems/increasing-triplet-subsequence/description/
#
# algorithms
# Medium (39.58%)
# Likes:    1103
# Dislikes: 105
# Total Accepted:    113.1K
# Total Submissions: 284.9K
# Testcase Example:  '[1,2,3,4,5]'
#
# Given an unsorted array return whether an increasing subsequence of length 3
# exists or not in the array.
# 
# Formally the function should:
# 
# Return true if there exists i, j, k 
# such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return
# false.
# 
# Note: Your algorithm should run in O(n) time complexity and O(1) space
# complexity.
# 
# 
# Example 1:
# 
# 
# Input: [1,2,3,4,5]
# Output: true
# 
# 
# 
# Example 2:
# 
# 
# Input: [5,4,3,2,1]
# Output: false
# 
# 
# 
#

# @lc code=start
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = float('inf')
        for x in nums:
            if x <= first:
                first = x
            elif x <= second:
                second = x
            else:
                return True
        return False
# @lc code=end

