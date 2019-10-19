#
# @lc app=leetcode id=274 lang=python3
#
# [274] H-Index
#
# https://leetcode.com/problems/h-index/description/
#
# algorithms
# Medium (34.89%)
# Likes:    452
# Dislikes: 776
# Total Accepted:    132.6K
# Total Submissions: 379.5K
# Testcase Example:  '[3,0,6,1,5]'
#
# Given an array of citations (each citation is a non-negative integer) of a
# researcher, write a function to compute the researcher's h-index.
# 
# According to the definition of h-index on Wikipedia: "A scientist has index h
# if h of his/her N papers have at least h citations each, and the other N − h
# papers have no more than h citations each."
# 
# Example:
# 
# 
# Input: citations = [3,0,6,1,5]
# Output: 3 
# Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each
# of them had 
# ⁠            received 3, 0, 6, 1, 5 citations respectively. 
# Since the researcher has 3 papers with at least 3 citations each and the
# remaining 
# two with no more than 3 citations each, her h-index is 3.
# 
# Note: If there are several possible values for h, the maximum one is taken as
# the h-index.
# 
#

# @lc code=start
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # Counting Sort
        n = len(citations)
        low, high = 0, n-1
        
        while low <= high:
            mid = (low + high) >> 1
            if citations[mid] < n - mid:
                low = mid + 1
            elif citations[mid] == n - mid:
                return citations[mid]
            else:
                high = mid - 1
        return n - low
        
# @lc code=end

