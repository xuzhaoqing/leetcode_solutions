#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#
# https://leetcode.com/problems/permutations/description/
#
# algorithms
# Medium (57.43%)
# Likes:    2581
# Dislikes: 84
# Total Accepted:    455.1K
# Total Submissions: 782.8K
# Testcase Example:  '[1,2,3]'
#
# Given a collection of distinct integers, return all possible permutations.
# 
# Example:
# 
# 
# Input: [1,2,3]
# Output:
# [
# ⁠ [1,2,3],
# ⁠ [1,3,2],
# ⁠ [2,1,3],
# ⁠ [2,3,1],
# ⁠ [3,1,2],
# ⁠ [3,2,1]
# ]
# 
# 
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ret = []
        def backtrack(remain, path):
            if len(remain) == 0:
                ret.append(path)
            else:
                for i in range(len(remain)):
                    backtrack(remain[:i]+remain[i+1:],[remain[i]] + path)
        backtrack(nums,[])
        return ret
        
# @lc code=end

