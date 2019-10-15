#
# @lc app=leetcode id=685 lang=python3
#
# [685] Redundant Connection II
#
# https://leetcode.com/problems/redundant-connection-ii/description/
#
# algorithms
# Hard (31.19%)
# Likes:    531
# Dislikes: 165
# Total Accepted:    26.3K
# Total Submissions: 84K
# Testcase Example:  '[[1,2],[1,3],[2,3]]'
#
# 
# In this problem, a rooted tree is a directed graph such that, there is
# exactly one node (the root) for which all other nodes are descendants of this
# node, plus every node has exactly one parent, except for the root node which
# has no parents.
# 
# The given input is a directed graph that started as a rooted tree with N
# nodes (with distinct values 1, 2, ..., N), with one additional directed edge
# added.  The added edge has two different vertices chosen from 1 to N, and was
# not an edge that already existed.
# 
# The resulting graph is given as a 2D-array of edges.  Each element of edges
# is a pair [u, v] that represents a directed edge connecting nodes u and v,
# where u is a parent of child v.
# 
# Return an edge that can be removed so that the resulting graph is a rooted
# tree of N nodes.  If there are multiple answers, return the answer that
# occurs last in the given 2D-array.
# Example 1:
# 
# Input: [[1,2], [1,3], [2,3]]
# Output: [2,3]
# Explanation: The given directed graph will be like this:
# ⁠ 1
# ⁠/ \
# v   v
# 2-->3
# 
# 
# Example 2:
# 
# Input: [[1,2], [2,3], [3,4], [4,1], [1,5]]
# Output: [4,1]
# Explanation: The given directed graph will be like this:
# 5  2
# ⁠    ^    |
# ⁠    |    v
# ⁠    4 
# 
# Note:
# The size of the input 2D-array will be between 3 and 1000.
# Every integer represented in the 2D-array will be between 1 and N, where N is
# the size of the input array.
# 
#

# @lc code=start
class UnionFind:
            def __init__(self, N):
                self.parents = [i for i in range(N+1)]
                self.ranks = [0 for _ in range(N+1)]

            def find(self,x):
                if x != self.parents[x]:
                    self.parents[x] = self.find(self.parents[x])
                return self.parents[x]

            def unite(self,x,y):
                x, y = self.find(x), self.find(y)
                if x == y:
                    return False

                if self.ranks[x] < self.ranks[y]:
                    self.parents[x] = self.parents[y]
                else:
                    self.parents[y] = self.parents[x]
                    if self.ranks[x] == self.ranks[y]:
                        self.ranks[x] += 1
                return True

class Solution:
    def findRedundantDirectedConnection(self, edges):
        c1, c2, parents = None, None, {}
        
        for u,v in edges:
            if v not in parents:
                parents[v] = u
            else:
                c1,c2 = [parents[v],v], [u,v]
                break
        uf = UnionFind(len(edges))
        
        for u,v in edges:
            if [u,v] == c2:
                continue
            if not uf.unite(u,v):
                if not c1:
                    return [u,v]
                else:
                    return c1
    
        return c2

# @lc code=end

# if __name__ == "__main__":
#     s = Solution()
#     edges = [[1,2],[1,3],[2,3]]
#     print(s.findRedundantDirectedConnection(edges))