class Solution:
    def circularPermutation(self, n: int, start: int):
        return [start ^ i ^ (i >> 1) for i in range(2**n)]
        # Got TLE
    #     if n == 1:
    #         return [start,1^start]
        
    #     total = 2 ** n
    #     self.ret = []
    #     def dfs(l,visited,last):
    #         if self.ret:
    #             return
    #         length = len(l)
    #         print(n,total)
    #         if length == total - 1:
    #             if self.isOneBit(last^l[-1]):
    #                     self.ret = l + [last]
        
           
    #         x = l[-1]
    #         print(n)
    #         for i in range(n):
    #             y = x ^ (1 << i)
    #             print(y)
    #             if y not in visited:
    #                 dfs(l+[y],visited|set([y]),last)
        
    #     for i in range(n):
    #         for j in range(n):
    #             if i != j:
    #                 y1 = start ^ (1 << i)
    #                 y2 = start ^ (1 << j)
    #                # print(y1,y2)
    #                 if not self.ret:
    #                     dfs([start,y1],set([start,y1,y2]),y2)
    #                 if not self.ret:
    #                     dfs([start,y2],set([start,y2,y1]),y1)
    #                 if self.ret:
    #                     return self.ret
        
    #     return self.ret
        
    # def isOneBit(self,x):
    #     while x > 0:
    #         if x & 1 == 1:
    #             return x == 1
    #         x = x >> 1
            
    #     return False
            

if __name__ == "__main__":
    s = Solution() 
    n,start = 12,1832
    print(s.circularPermutation(n,start))