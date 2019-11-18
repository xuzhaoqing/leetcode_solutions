# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class FindElements:

    def __init__(self, root: TreeNode):
        root.val = 0
        q = deque([root])
        while q:
            node = q.popleft()
            if node.left:
                node.left.val = 2 * node.val + 1
                q.append(node.left)
            if node.right:
                node.right.val = 2 * node.val + 2
                q.append(node.right)
        self.root = root
                
    def find(self, target: int) -> bool:
        c = bin(target+1)[3:]
        index = 0
        root = self.root
        while root and index <= len(c):
            if root.val == target:
                return True
            if c[index] == '0':
                root = root.left
            else:
                root = root.right
            index += 1
        return False
            


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)