from collections import defaultdict
class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        M,N = len(grid), len(grid[0])
        dp = defaultdict(int)
        
        for i in range(M):           
            count = 0
            for j in range(N):
                if grid[i][j] == 'E':
                    count += 1
                elif grid[i][j] == 'W':
                    count = 0
                else:
                    dp[i,j] += count
            
            count = 0
            for j in range(N-1,-1,-1):
                if grid[i][j] == 'E':
                    count += 1
                elif grid[i][j] == 'W':
                    count = 0
                else:
                    dp[i,j] += count
        
        for j in range(N):
            count = 0
            for i in range(M):
                if grid[i][j] == 'E':
                    count += 1
                elif grid[i][j] == 'W':
                    count = 0
                else:
                    dp[i,j] += count
            
            count = 0
            for i in range(M-1,-1,-1):
                if grid[i][j] == 'E':
                    count += 1
                elif grid[i][j] == 'W':
                    count = 0
                else:
                    dp[i,j] += count
        if not dp:
            return 0
        
        return max(dp.values())