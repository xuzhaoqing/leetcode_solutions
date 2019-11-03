from collections import defaultdict
from functools import lru_cache
class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        @lru_cache(None)
        def dfs(curr,parent):
            if len(d[curr]) == 1 and d[curr][0] == parent:
                return 1
            else:
                return max([dfs(c,curr) for c in d[curr] if c != parent]) + 1
        
        d = defaultdict(list)
        for e in edges:
            x,y = e
            d[x].append(y)
            d[y].append(x)
        
        self.m = 0
        for i in d:
            if len(d[i]) > 1:
                l = []
                for j in d[i]:
                    l.append(dfs(j,i))
                l.sort()
                self.m = max(self.m, l[-1] + l[-2])
        
        if self.m == 0:
            return len(d)
        
       
        return self.m