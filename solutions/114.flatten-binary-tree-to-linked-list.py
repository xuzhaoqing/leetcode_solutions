#
# @lc app=leetcode id=114 lang=python3
#
# [114] Flatten Binary Tree to Linked List
#
# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/
#
# algorithms
# Medium (44.16%)
# Likes:    1826
# Dislikes: 241
# Total Accepted:    271.4K
# Total Submissions: 608.1K
# Testcase Example:  '[1,2,5,3,4,null,6]'
#
# Given a binary tree, flatten it to a linked list in-place.
# 
# For example, given the following tree:
# 
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   5
# ⁠/ \   \
# 3   4   6
# 
# 
# The flattened tree should look like:
# 
# 
# 1
# ⁠\
# ⁠ 2
# ⁠  \
# ⁠   3
# ⁠    \
# ⁠     4
# ⁠      \
# ⁠       5
# ⁠        \
# ⁠         6
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        # 思路是先flatten root.left, 然后找到root.left的末尾，再把root.right flatten之后插到这里
        if not root:
            return root
        
        
        if root.left:
            root.left = self.flatten(root.left)
            p = root.left
            while p.right:
                p = p.right
            root.right = self.flatten(root.right)
            p.right = root.right
            root.right = root.left
            root.left = None
        else:
            root.right = self.flatten(root.right)
        return root
            
# @lc code=end

