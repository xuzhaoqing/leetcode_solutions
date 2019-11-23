#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#
# https://leetcode.com/problems/copy-list-with-random-pointer/description/
#
# algorithms
# Medium (28.88%)
# Likes:    2151
# Dislikes: 526
# Total Accepted:    309.3K
# Total Submissions: 1M
# Testcase Example:  '{"$id":"1","next":{"$id":"2","next":null,"random":{"$ref":"2"},"val":2},"random":{"$ref":"2"},"val":1}'
#
# A linked list is given such that each node contains an additional random
# pointer which could point to any node in the list or null.
# 
# Return a deep copy of the list.
# 
# 
# 
# Example 1:
# 
# 
# 
# 
# Input:
# 
# {"$id":"1","next":{"$id":"2","next":null,"random":{"$ref":"2"},"val":2},"random":{"$ref":"2"},"val":1}
# 
# Explanation:
# Node 1's value is 1, both of its next and random pointer points to Node 2.
# Node 2's value is 2, its next pointer points to null and its random pointer
# points to itself.
# 
# 
# 
# 
# Note:
# 
# 
# You must return the copy of the given head as a reference to the cloned
# list.
# 
# 
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        # ????????????????
        # ?????????????node??duplicate??node
        
        p = head
        while p:
            node = Node(p.val,p.next,None)
            p.next = node
            p = node.next
            
        p = head
        while p:
            if not p.random:
                p.next.random = None
            else:
                p.next.random = p.random.next
            p = p.next.next
        
        p = head
        dummy = Node(0,None,None)
        p2 = dummy
        while p:
            p2.next = p.next
            p.next = p.next.next
            p = p.next
            p2 = p2.next
        return dummy.next
    
#         dic = {None: None}
#         node = head
#         while node:
#             copy = Node(node.val, None, None)
#             dic[node] = copy
#             node = node.next
        
#         node = head
#         while node:
#             dic[node].next = dic[node.next]
#             dic[node].random = dic[node.random]
#             node = node.next
#         return dic[head]
        
# @lc code=end

