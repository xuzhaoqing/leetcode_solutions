#
# @lc app=leetcode id=930 lang=python3
#
# [930] Binary Subarrays With Sum
#
# https://leetcode.com/problems/binary-subarrays-with-sum/description/
#
# algorithms
# Medium (39.43%)
# Likes:    292
# Dislikes: 15
# Total Accepted:    13.2K
# Total Submissions: 33.2K
# Testcase Example:  '[1,0,1,0,1]\n2'
#
# In an array A of 0s and 1s, how many non-empty subarrays have sum S?
# 
# 
# 
# Example 1:
# 
# 
# Input: A = [1,0,1,0,1], S = 2
# Output: 4
# Explanation: 
# The 4 subarrays are bolded below:
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
# 
# 
# 
# 
# Note:
# 
# 
# A.length <= 30000
# 0 <= S <= A.length
# A[i] is either 0 or 1.
# 
#

# @lc code=start

import collections
class Solution(object):
    def numSubarraysWithSum(self, A, S):
        # Use Prefix- Sum
        count = collections.Counter({0:1})
        pres = res = 0
        for x in A:
            pres += x
            res += count[pres-S]
            count[pres] += 1
        return res
# @lc code=end

