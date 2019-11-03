class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        nums = [n%2 for n in nums]
        odds = [i for i,n in enumerate(nums) if n == 1]
        N = len(nums)

        ret = 0
        for i in range(len(odds)-k+1):
            
            if i == 0:
                a = odds[i] + 1
            else:
                a = odds[i] - odds[i-1]
            
            if i+k-1 == len(odds)-1:
                b = len(nums) - odds[i+k-1]
            else:
                b = odds[i+k] - odds[i+k-1]
            ret += a * b
        return ret
    
#         dp = [[-1 for _ in range(N)] for _ in range(N)]
#         m = 0
#         for end in range(k-1,N):
#             for start in range(end+2-k):
#                 if start == end:
#                     dp[start][end] = nums[end] 
#                 elif dp[start][end-1] == -1:
#                     dp[start][end] = sum(nums[start:end+1])
#                 else:
#                     dp[start][end] = dp[start][end-1] + nums[end]
                
#                 if dp[start][end] == k:
#                     m += 1
#         return m