#
# @lc app=leetcode id=132 lang=python3
#
# [132] Palindrome Partitioning II
#
# https://leetcode.com/problems/palindrome-partitioning-ii/description/
#
# algorithms
# Hard (28.28%)
# Likes:    737
# Dislikes: 26
# Total Accepted:    113.9K
# Total Submissions: 398.4K
# Testcase Example:  '"aab"'
#
# Given a string s, partition s such that every substring of the partition is a
# palindrome.
# 
# Return the minimum cuts needed for a palindrome partitioning of s.
# 
# Example:
# 
# 
# Input: "aab"
# Output: 1
# Explanation: The palindrome partitioning ["aa","b"] could be produced using 1
# cut.
# 
# 
#

# @lc code=start
class Solution:
    def minCut(self, s: str) -> int:
        N = len(s)
        if N == 0:
            return 0
        isPalindrome = [[False for _ in range(N)] for _ in range(N)]
        cuts = [i for i in range(1,N+1)]
        
        for end in range(N):
            for start in range(end+1):
                if s[start] == s[end] and (end - start < 2 or isPalindrome[start+1][end-1]):
                    isPalindrome[start][end] = True
                    if start == 0:
                        cuts[end] = 0
                    else:
                        cuts[end] = min(cuts[end],cuts[start-1] + 1)
        
        return cuts[N-1]
        
# @lc code=end

