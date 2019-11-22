#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#
# https://leetcode.com/problems/lru-cache/description/
#
# algorithms
# Medium (27.31%)
# Likes:    3984
# Dislikes: 162
# Total Accepted:    387.3K
# Total Submissions: 1.4M
# Testcase Example:  '["LRUCache","put","put","get","put","get","put","get","get","get"]\n' +
#  '[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]'
#
# Design and implement a data structure for Least Recently Used (LRU) cache. It
# should support the following operations: get and put.
# 
# get(key) - Get the value (will always be positive) of the key if the key
# exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present.
# When the cache reached its capacity, it should invalidate the least recently
# used item before inserting a new item.
# 
# The cache is initialized with a positive capacity.
# 
# Follow up:
# Could you do both operations in O(1) time complexity?
# 
# Example:
# 
# 
# LRUCache cache = new LRUCache( 2 /* capacity */ );
# 
# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // returns 1
# cache.put(3, 3);    // evicts key 2
# cache.get(2);       // returns -1 (not found)
# cache.put(4, 4);    // evicts key 1
# cache.get(1);       // returns -1 (not found)
# cache.get(3);       // returns 3
# cache.get(4);       // returns 4
# 
# 
# 
# 
#

# @lc code=start
class Node:
    def __init__(self,key,value):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.dict = {}
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
        
        self._update(key)
        return self.dict[key].val
    
    def _update(self,key):
        node = self.dict[key]
        self._remove(node)
        self._add(node)
    
    def _remove(self,node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p
    
    
    def _add(self,node):
        p = self.tail.prev
        p.next = node
        node.prev = p
        node.next = self.tail
        self.tail.prev = node
        
        
    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self._update(key)
            self.tail.prev.val = value
        else:
            node = Node(key,value)
            self.dict[key] = node
            self._add(node)
            if len(self.dict) > self.cap:
                key = self.head.next.key
                self._remove(self.head.next)
                del self.dict[key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

