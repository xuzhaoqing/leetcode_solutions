#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#
# https://leetcode.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (27.92%)
# Likes:    4626
# Dislikes: 417
# Total Accepted:    697.3K
# Total Submissions: 2.5M
# Testcase Example:  '"babad"'
#
# Given a string s, find the longest palindromic substring in s. You may assume
# that the maximum length of s is 1000.
# 
# Example 1:
# 
# 
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# 
# 
# Example 2:
# 
# 
# Input: "cbbd"
# Output: "bb"
# 
# 
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        N = len(s)
        maxLength, maxStart, maxEnd = 0, 0, 0
        dp = [[False for _ in range(N)] for _ in range(N)]
        for end in range(N):
            for start in range(end,-1,-1):
                if start == end:
                    dp[start][end] = True
                elif start + 1 == end:
                    dp[start][end] = s[start] == s[end]
                else:
                    dp[start][end] = s[start] == s[end] and dp[start+1][end-1]

                if dp[start][end] and end - start + 1 > maxLength:
                    maxLength = end - start + 1
                    maxStart, maxEnd = start,end
        return s[maxStart:maxEnd+1]

if __name__ == "__main__":
    s = Solution()
    string = "babad"
    print(s.longestPalindrome(string))
# @lc code=end

