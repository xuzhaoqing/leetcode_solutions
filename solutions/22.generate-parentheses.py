#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#
# https://leetcode.com/problems/generate-parentheses/description/
#
# algorithms
# Medium (57.04%)
# Likes:    3472
# Dislikes: 206
# Total Accepted:    411K
# Total Submissions: 712.2K
# Testcase Example:  '3'
#
# 
# Given n pairs of parentheses, write a function to generate all combinations
# of well-formed parentheses.
# 
# 
# 
# For example, given n = 3, a solution set is:
# 
# 
# [
# ⁠ "((()))",
# ⁠ "(()())",
# ⁠ "(())()",
# ⁠ "()(())",
# ⁠ "()()()"
# ]
# 
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.ret = []

        def backtrack(par,left,right):
            if left == 0 and right == 0:
                self.ret.append(''.join(par))
            
            if left > 0:
                backtrack(par+['('], left-1,right)
            
            if right > left:
                backtrack(par+[')'], left, right-1)
        backtrack([],n,n)
        return self.ret

# @lc code=end

