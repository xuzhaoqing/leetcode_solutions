#
# @lc app=leetcode id=713 lang=python3
#
# [713] Subarray Product Less Than K
#
# https://leetcode.com/problems/subarray-product-less-than-k/description/
#
# algorithms
# Medium (37.46%)
# Likes:    821
# Dislikes: 41
# Total Accepted:    40.3K
# Total Submissions: 106.3K
# Testcase Example:  '[10,5,2,6]\n100'
#
# Your are given an array of positive integers nums.
# Count and print the number of (contiguous) subarrays where the product of all
# the elements in the subarray is less than k.
# 
# Example 1:
# 
# Input: nums = [10, 5, 2, 6], k = 100
# Output: 8
# Explanation: The 8 subarrays that have product less than 100 are: [10], [5],
# [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
# Note that [10, 5, 2] is not included as the product of 100 is not strictly
# less than k.
# 
# 
# 
# Note:
# 0 < nums.length .
# 0 < nums[i] < 1000.
# 0 .
# 
#

# @lc code=start
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if not nums or k <= 1:
            return 0
        start, prod, ans = 0, 1, 0
        N = len(nums)
        for end in range(N):
            prod *= nums[end]
            while prod >= k:
                prod //= nums[start]
                start += 1
            ans += end - start + 1
        return ans
# @lc code=end

