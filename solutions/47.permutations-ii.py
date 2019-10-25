#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#
# https://leetcode.com/problems/permutations-ii/description/
#
# algorithms
# Medium (42.20%)
# Likes:    1320
# Dislikes: 46
# Total Accepted:    282.7K
# Total Submissions: 661.6K
# Testcase Example:  '[1,1,2]'
#
# Given a collection of numbers that might contain duplicates, return all
# possible unique permutations.
# 
# Example:
# 
# 
# Input: [1,1,2]
# Output:
# [
# ⁠ [1,1,2],
# ⁠ [1,2,1],
# ⁠ [2,1,1]
# ]
# 
# 
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ret = []
        nums.sort()
        def dfs(remain,path):
            if len(remain) == 0:
                ret.append(path)
            else:
                for i in range(len(remain)):
                    if i and remain[i-1] == remain[i]:
                        continue
                    else:
                        dfs(remain[:i] + remain[i+1:],path+[remain[i]])
        dfs(nums,[])
        return ret
# @lc code=end

