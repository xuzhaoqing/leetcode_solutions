#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#
# https://leetcode.com/problems/word-ladder/description/
#
# algorithms
# Medium (25.55%)
# Likes:    1924
# Dislikes: 910
# Total Accepted:    310.3K
# Total Submissions: 1.2M
# Testcase Example:  '"hit"\n"cog"\n["hot","dot","dog","lot","log","cog"]'
#
# Given two words (beginWord and endWord), and a dictionary's word list, find
# the length of shortest transformation sequence from beginWord to endWord,
# such that:
# 
# 
# Only one letter can be changed at a time.
# Each transformed word must exist in the word list. Note that beginWord is not
# a transformed word.
# 
# 
# Note:
# 
# 
# Return 0 if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.
# 
# 
# Example 1:
# 
# 
# Input:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
# 
# Output: 5
# 
# Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" ->
# "dog" -> "cog",
# return its length 5.
# 
# 
# Example 2:
# 
# 
# Input:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
# 
# Output: 0
# 
# Explanation: The endWord "cog" is not in wordList, therefore no possible
# transformation.
# 
# 
# 
# 
# 
#

# @lc code=start
from collections import defaultdict, deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # ???????BFS????????wordList??word??word[:i]+'*'+word[i+1:]??
        if not wordList or not beginWord or not endWord or endWord not in wordList:
            return 0
        queue = deque()
        all_intermediate_states = defaultdict(list)
        L = len(beginWord)
        for word in wordList:
            for i in range(L):
                state = word[:i] + '*' + word[i+1:]
                all_intermediate_states[state].append(word)
        visited = set([beginWord])
        queue.append((beginWord,1))
        
        while queue:
            word, step = queue.popleft()
            if word == endWord:
                return step
            for i in range(L):
                state = word[:i] + '*' + word[i+1:]
                for pot_word in all_intermediate_states[state]:
                    if pot_word not in visited:
                        queue.append((pot_word,step+1))
                        visited.add(pot_word)
        return 0




# @lc code=end

