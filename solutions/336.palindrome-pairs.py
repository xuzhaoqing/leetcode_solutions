#
# @lc app=leetcode id=336 lang=python3
#
# [336] Palindrome Pairs
#
# https://leetcode.com/problems/palindrome-pairs/description/
#
# algorithms
# Hard (31.83%)
# Likes:    981
# Dislikes: 132
# Total Accepted:    83.1K
# Total Submissions: 258.2K
# Testcase Example:  '["abcd","dcba","lls","s","sssll"]'
#
# Given a list of unique words, find all pairs of distinct indices (i, j) in
# the given list, so that the concatenation of the two words, i.e. words[i] +
# words[j] is a palindrome.
# 
# Example 1:
# 
# 
# 
# Input: ["abcd","dcba","lls","s","sssll"]
# Output: [[0,1],[1,0],[3,2],[2,4]] 
# Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]
# 
# 
# 
# Example 2:
# 
# 
# Input: ["bat","tab","cat"]
# Output: [[0,1],[1,0]] 
# Explanation: The palindromes are ["battab","tabbat"]
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def palindromePairs(self, words):
        
        

if __name__ == "__main__":
    s = Solution()
    words = ["abcd","dcba","lls","s","sssll"]
    print(s.palindromePairs(words))
        
        
        # Brute Force O(n**3)
        
        
        
# @lc code=end

