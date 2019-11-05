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
        def dfs(plist,remained):
            if not remained:
                ret.append(plist) 
                return
            
            for i in range(1,len(remained)+1):
                if remained[:i][::-1] == remained[:i]:
                    dfs(plist+[remained[:i]], remained[i:])
        dfs([],s)
        return ret
        
# @lc code=end

