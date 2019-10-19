#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#
# https://leetcode.com/problems/palindrome-partitioning/description/
#
# algorithms
# Medium (42.72%)
# Likes:    1170
# Dislikes: 48
# Total Accepted:    185.5K
# Total Submissions: 430.2K
# Testcase Example:  '"aab"'
#
# Given a string s, partition s such that every substring of the partition is a
# palindrome.
# 
# Return all possible palindrome partitioning of s.
# 
# Example:
# 
# 
# Input: "aab"
# Output:
# [
# ⁠ ["aa","b"],
# ⁠ ["a","a","b"]
# ]
# 
# 
#

# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ret = []

        def dfs(remain,path):
            if not remain:
                ret.append(path)
            
            for i in range(1,len(remain)+1):
                if isPal(remain[:i]):
                    dfs(remain[i:], path + [remain[:i]])
        def isPal(st):
            return st == st[::-1]
        
        dfs(s,[])
        return ret
        
# @lc code=end

