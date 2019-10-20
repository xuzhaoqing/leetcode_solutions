class Solution:
    def probabilityOfHeads(self, prob, target: int) -> float:
        # 试了一下DFS的方法，只得到了 TLE
        N = len(prob)
        dp = [[0 for _ in range(target+1)] for _ in range(N+1)] # 前c个硬币里面有k个翻面的
        dp[0] = [1] + [0] * target
        for i,p in enumerate(prob,1):
            for k in range(target+1):
                dp[i][k] = (dp[i-1][k-1] if k else 0) * p + dp[i-1][k] * (1-p)
        return dp[N][target]


if __name__ == "__main__":
    s = Solution()
    prob, target = [0.5,0.5,0.5,0.5,0.5], 0
    print(s.probabilityOfHeads(prob,target))