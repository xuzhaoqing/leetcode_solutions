#
# @lc app=leetcode id=1110 lang=python3
#
# [1110] Delete Nodes And Return Forest
#
# https://leetcode.com/problems/delete-nodes-and-return-forest/description/
#
# algorithms
# Medium (63.69%)
# Likes:    410
# Dislikes: 11
# Total Accepted:    19.2K
# Total Submissions: 30.1K
# Testcase Example:  '[1,2,3,4,5,6,7]\n[3,5]'
#
# Given the root of a binary tree, each node in the tree has a distinct value.
# 
# After deleting all nodes with a value in to_delete, we are left with a forest
# (a disjoint union of trees).
# 
# Return the roots of the trees in the remaining forest.  You may return the
# result in any order.
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
# Output: [[1,2,null,4],[6],[7]]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the given tree is at most 1000.
# Each node has a distinct value between 1 and 1000.
# to_delete.length <= 1000
# to_delete contains distinct values between 1 and 1000.
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
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        ret = []
        to_delete = set(to_delete)
        def helper(node, is_root):
            if not node: return None
            is_delete_root = node.val in to_delete
            if not is_delete_root and is_root:
                ret.append(node)
            
            node.left = helper(node.left, is_delete_root)
            node.right = helper(node.right, is_delete_root)
            return None if is_delete_root else node
        helper(root,True)        
        return ret
    
# @lc code=end

