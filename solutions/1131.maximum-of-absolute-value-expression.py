#
# @lc app=leetcode id=1131 lang=python3
#
# [1131] Maximum of Absolute Value Expression
#
# https://leetcode.com/problems/maximum-of-absolute-value-expression/description/
#
# algorithms
# Medium (51.83%)
# Likes:    72
# Dislikes: 91
# Total Accepted:    4.3K
# Total Submissions: 8.3K
# Testcase Example:  '[1,2,3,4]\n[-1,4,5,6]'
#
# Given two arrays of integers with equal lengths, return the maximum value
# of:
# 
# |arr1[i] - arr1[j]| + |arr2[i] - arr2[j]| + |i - j|
# 
# where the maximum is taken over all 0 <= i, j < arr1.length.
# 
# 
# Example 1:
# 
# 
# Input: arr1 = [1,2,3,4], arr2 = [-1,4,5,6]
# Output: 13
# 
# 
# Example 2:
# 
# 
# Input: arr1 = [1,-2,-5,0,10], arr2 = [0,-2,-1,-7,-4]
# Output: 20
# 
# 
# 
# Constraints:
# 
# 
# 2 <= arr1.length == arr2.length <= 40000
# -10^6 <= arr1[i], arr2[i] <= 10^6
# 
# 
#

# @lc code=start
class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        # Brute Force O(N^2)
        # def f(i,j):
        #     return abs(arr1[i]-arr1[j]) + abs(arr2[i]-arr2[j]) + abs(i-j) 
        # m = 0
        # for i in range(len(arr1)):
        #     for j in range(len(arr2)):
        #         m = max(m,f(i,j))
        # return m
        
        # Math
        # Assume i > j, since if i <= j, we could change them, with abs, it's actually the same
        # There are four possible results
        # 1. arr1[i] - arr1[j] + arr2[i] - arr2[j] + i - j = (arr1[i]+arr2[i]+i) - (arr1[j]+arr2[j]+j)
        # 2. arr1[i] - arr1[j] + arr2[j] - arr2[i] + i - j = (arr1[i]-arr2[i]+i) - (arr1[j]-arr2[j]+j)
        # 3. -arr1[i] + arr1[j] + arr2[i] - arr2[j] + i - j = (arr2[i]-arr1[i]+i) - (arr2[j]-arr1[j]+j)
        # 4. -arr1[i] + arr1[j] + arr2[j] - arr2[i] + i - j = (-arr2[i]-arr1[i]+i) - (-arr2[j]-arr1[j]+j)
        l1,l2,l3,l4 = [], [], [], []
        for i in range(len(arr1)):
            l1.append(arr1[i]+arr2[i]+i)
            l2.append(arr1[i]-arr2[i]+i)
            l3.append(-arr1[i]+arr2[i]+i)
            l4.append(-arr1[i]-arr2[i]+i)
        return max(map(lambda x: max(x)-min(x), [l1,l2,l3,l4]))
        
# @lc code=end

