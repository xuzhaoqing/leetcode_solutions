#
# @lc app=leetcode id=126 lang=python3
#
# [126] Word Ladder II
#
# https://leetcode.com/problems/word-ladder-ii/description/
#
# algorithms
# Hard (18.89%)
# Likes:    1252
# Dislikes: 213
# Total Accepted:    140.9K
# Total Submissions: 734.4K
# Testcase Example:  '"hit"\n"cog"\n["hot","dot","dog","lot","log","cog"]'
#
# Given two words (beginWord and endWord), and a dictionary's word list, find
# all shortest transformation sequence(s) from beginWord to endWord, such
# that:
# 
# 
# Only one letter can be changed at a time
# Each transformed word must exist in the word list. Note that beginWord is not
# a transformed word.
# 
# 
# Note:
# 
# 
# Return an empty list if there is no such transformation sequence.
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
# Output:
# [
# ⁠ ["hit","hot","dot","dog","cog"],
# ["hit","hot","lot","log","cog"]
# ]
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
# Output: []
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
from collections import  defaultdict
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        # ???????????????????????????????????BFS??????????????layer?????BFS????????????
        if not beginWord or not endWord or not wordList or endWord not in wordList:
            return []
        queue = []
        all_intermediate_states = defaultdict(list)
        L = len(beginWord)
        for word in wordList:
            for i in range(L):
                state = word[:i] + '*' + word[i+1:]
                all_intermediate_states[state].append(word)
        
        visited = set([beginWord])
        queue.append([beginWord])
        while queue and len(queue[0]) <= len(wordList):
            new_queue = []
            for wlist in queue:
                if wlist[-1] == endWord:
                    return [wlist for wlist in queue if wlist[-1] == endWord]
                
                word = wlist[-1]
                for i in range(L):
                    state = word[:i] + '*' + word[i+1:]
                    for w in all_intermediate_states[state]:
                        if w not in visited:
                            new_queue.append(wlist + [w])
                
            for wlist in new_queue:
                visited.add(wlist[-1])
        return []
        
# @lc code=end

