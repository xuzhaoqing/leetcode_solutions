#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#
# https://leetcode.com/problems/median-of-two-sorted-arrays/description/
#
# algorithms
# Hard (27.30%)
# Likes:    5326
# Dislikes: 779
# Total Accepted:    538.7K
# Total Submissions: 1.9M
# Testcase Example:  '[1,3]\n[2]'
#
# There are two sorted arrays nums1 and nums2 of size m and n respectively.
# 
# Find the median of the two sorted arrays. The overall run time complexity
# should be O(log (m+n)).
# 
# You may assume nums1 and nums2 cannot be both empty.
# 
# Example 1:
# 
# 
# nums1 = [1, 3]
# nums2 = [2]
# 
# The median is 2.0
# 
# 
# Example 2:
# 
# 
# nums1 = [1, 2]
# nums2 = [3, 4]
# 
# The median is (2 + 3)/2 = 2.5
# 
# 
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        N = len(nums1) + len(nums2)
        isodd = N % 2
        isp1 = True
        p1,p2,count = 0,0,0
        
        while True:
            if p2 < len(nums2) and (p1 >= len(nums1) or nums1[p1] >= nums2[p2]):
                # count += 1
                p2 += 1
                isp1 = False
            else:
                p1 += 1
                isp1 = True
            count += 1
            
            if isodd and count == (N+1)//2:
                if isp1:
                    return nums1[p1-1]
                else:
                    return nums2[p2-1]
            elif not isodd and count == N // 2:
                if isp1:
                    if p2 < len(nums2) and (p1 >= len(nums1) or nums1[p1] >= nums2[p2]):
                        return (nums1[p1-1] + nums2[p2])/2
                    else:
                        return (nums1[p1-1] + nums1[p1])/2
                else:
                    if p2 < len(nums2) and (p1 >= len(nums1) or nums1[p1] >= nums2[p2]):
                        return (nums2[p2-1] + nums2[p2])/2
                    else:
                        return (nums2[p2-1] + nums1[p1])/2

# @lc code=end

