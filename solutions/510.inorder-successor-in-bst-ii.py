"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, parent):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent
"""
class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Node':
        if not node:
            return None
        
        if node.right:
            node = node.right
            while node.left:
                node = node.left
            return node
        
       
        while node.parent:
            if node.parent.left == node:
                return node.parent
            node = node.parent
        
        return None
        
       