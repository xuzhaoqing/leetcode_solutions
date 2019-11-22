class Solution:
    def minimumCost(self, N: int, connections: List[List[int]]) -> int:
        # Union Find 
    
        class UnionFind:
            def __init__(self,n):
                self.parents = list(range(n))
                self.ranks = [0] * n
                self.len = n
            def find(self,x):
                if x != self.parents[x]:
                    self.parents[x] = self.find(self.parents[x])
                return self.parents[x]
            
            def union(self,x,y):
                x,y = self.find(x), self.find(y)
                if x == y:
                    return False
                self.len -= 1
                if(self.ranks[x] < self.ranks[y]):
                    self.parents[x] = y
                else:
                    self.parents[y]= x
                    if self.ranks[x] == self.ranks[y]:
                        self.ranks[x] += 1
                return True
            
            
        uf = UnionFind(N)
        connections = sorted(connections,key = lambda x:x[2])
        
        cost = 0
        for n1,n2, c in connections:
            if uf.union(n1-1,n2-1):
                cost += c
            
            if uf.len == 1:
                return cost
        return -1
        
        
        