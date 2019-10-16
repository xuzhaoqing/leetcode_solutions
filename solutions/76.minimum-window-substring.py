#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#
# https://leetcode.com/problems/minimum-window-substring/description/
#
# algorithms
# Hard (31.93%)
# Likes:    2903
# Dislikes: 206
# Total Accepted:    285.5K
# Total Submissions: 887.4K
# Testcase Example:  '"ADOBECODEBANC"\n"ABC"'
#
# Given a string S and a string T, find the minimum window in S which will
# contain all the characters in T in complexity O(n).
# 
# Example:
# 
# 
# Input: S = "ADOBECODEBANC", T = "ABC"
# Output: "BANC"
# 
# 
# Note:
# 
# 
# If there is no such window in S that covers all characters in T, return the
# empty string "".
# If there is such window, you are guaranteed that there will always be only
# one unique minimum window in S.
# 
# 
#

# @lc code=start
from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #这个题是真的不容易，需要总结一下
        #1. 这种题的解题思路：2 pointers + hashMap
        #2. 需要用到enumerate(s,1)这种形式
        head = 0
        hashMap,missing = Counter(t), len(t)
        start, end = 0,0
        for rear, c in enumerate(s,1):
            missing -= hashMap[c] > 0
            hashMap[c] -= 1
            
            if missing <= 0:
                while  hashMap[s[head]] < 0:
                    hashMap[s[head]] += 1
                    head += 1
                
                if not end or rear - head <= end - start:
                    start,end = head, rear
                hashMap[s[head]] += 1
                head += 1
                missing += 1
     
        return s[start:end]
# @lc code=end

if __name__ == "__main__":
    sol = Solution()
    S = "ADOBECODEBANC"
    T = "ABC"
    print(sol.minWindow(S,T))