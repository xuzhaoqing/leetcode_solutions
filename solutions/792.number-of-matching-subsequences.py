#
# @lc app=leetcode id=792 lang=python3
#
# [792] Number of Matching Subsequences
#
# https://leetcode.com/problems/number-of-matching-subsequences/description/
#
# algorithms
# Medium (44.75%)
# Likes:    607
# Dislikes: 44
# Total Accepted:    28.3K
# Total Submissions: 62K
# Testcase Example:  '"abcde"\n["a","bb","acd","ace"]'
#
# Given string S and a dictionary of words words, find the number of words[i]
# that is a subsequence of S.
# 
# 
# Example :
# Input: 
# S = "abcde"
# words = ["a", "bb", "acd", "ace"]
# Output: 3
# Explanation: There are three words in words that are a subsequence of S: "a",
# "acd", "ace".
# 
# 
# Note:
# 
# 
# All words in words and S will only consists of lowercase letters.
# The length of S will be in the range of [1, 50000].
# The length of words will be in the range of [1, 5000].
# The length of words[i] will be in the range of [1, 50].
# 
# 
#

# @lc code=start
class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        # bucket
        heads = collections.defaultdict(list)
        for word in words:
            heads[word[0]].append(word)
        count = 0
        for c in S:
            allWords = heads[c]
            heads[c] = []
            for word in allWords:
                w = word[1:]
                if w:
                    heads[w[0]].append(w)
                else:
                    count += 1
        return count     
# @lc code=end

