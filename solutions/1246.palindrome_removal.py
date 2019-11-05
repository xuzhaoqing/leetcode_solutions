class Solution:
    def minimumMoves(self, arr: List[int]) -> int:
        N = len(arr)
        dp = [[0 for _ in range(N)] for _ in range(N)]
        
        for i in range(N):
            dp[i][i] = 1
            if i != N-1:
                dp[i][i+1] = 1 if arr[i] == arr[i+1] else 2
        
        for size in range(3,N+1):
            for start in range(N-size+1):
                end = start + size - 1
                if arr[start] == arr[end]:
                    dp[start][end] = dp[start+1][end-1]
                else:
                    dp[start][end] = min([dp[start][mid] + dp[mid+1][end] for mid in range(start,end)])
        return dp[0][N-1]
        
        
        
        