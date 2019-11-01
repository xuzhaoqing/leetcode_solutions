class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        dist = []
        for i in range(len(workers)):
            for j in range(len(bikes)):
                dist.append((self.distance(workers[i],bikes[j]),i,j))
        
        ret = [-1] * len(workers)
        visited = set()
        
        dist.sort()
        for _, i,j in dist:
            if ret[i] == -1 and j not in visited:
                ret[i] = j
                visited.add(j)
        return ret
    
    def distance(self,worker,bike):
        return abs(worker[0]-bike[0]) + abs(worker[1]-bike[1])