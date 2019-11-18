class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [[0,0,0] for _ in range(len(nums)+1)]
        for i in range(1,len(nums)+1):
            n = nums[i-1]
            new_res = set(n+x for x in dp[i-1])
            c = dict(zip(range(3),dp[i-1]))
            for x in new_res:
                c[x%3] = max(x,c[x%3])
            
            dp[i] = list(c.values())
        return dp[len(nums)][0]
            