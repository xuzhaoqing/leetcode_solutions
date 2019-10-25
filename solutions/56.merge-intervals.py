#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#
# https://leetcode.com/problems/merge-intervals/description/
#
# algorithms
# Medium (36.64%)
# Likes:    2698
# Dislikes: 212
# Total Accepted:    432.1K
# Total Submissions: 1.2M
# Testcase Example:  '[[1,3],[2,6],[8,10],[15,18]]'
#
# Given a collection of intervals, merge all overlapping intervals.
# 
# Example 1:
# 
# 
# Input: [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into
# [1,6].
# 
# 
# Example 2:
# 
# 
# Input: [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
# 
# NOTE: input types have been changed on April 15, 2019. Please reset to
# default code definition to get new method signature.
# 
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals or len(intervals) == 1:
            return intervals
        
        intervals.sort(key=lambda x:x[0])
        i = 0
        
        while(i < len(intervals)-1):
            if intervals[i][1] >= intervals[i+1][0]:
                intervals[i][1] = max(intervals[i][1],intervals[i+1][1])
                intervals.pop(i+1)
            else:
                i += 1
        return intervals
# @lc code=end

