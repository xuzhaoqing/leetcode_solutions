"""
This file is about the code snippets I wrote for dynamic programming algorithmic problems
"""
from basicDS import TreeNode


# 1.  Maximum Subarray (53)  求和最大的子序列 

def maxSubArray(nums):
    for i in range(1, len(nums)):
        if nums[i-1] > 0:
            nums[i] += nums[i-1] 
    return max(nums)

# @2019.09.15

# 2.  Longest Palindromic Substring (Leetcode 5) 最长回文子串

def longestPalindrome(s):
    if not s:
        return 0
    N = len(s)
    dp = [[False for _ in range(N)] for _ in range(N)]
    maxLength = 0
    for end in range(N):
        for start in range(end,-1,-1):
            if start == end:
                dp[start][end] = True
            elif start + 1 == end:
                dp[start][end] = s[start] == s[end]
            else:
                dp[start][end] = (s[start] == s[end] and dp[start+1][end-1])

            if dp[start][end]:
                maxLength = max(maxLength, end - start + 1)
    return maxLength

arr = [1,2,-3,4,-7,2,1,4]
print("maxSubArray:", maxSubArray(arr))

# 3. Longest Valid Parentheses (Leetcode 32) 最长合理括号对
def longestValidParentheses(s):
    # Too hard for me now
    pass

# 4. Unique Paths (Leetcode 62) 独一无二的路径

def uniquePaths(m , n):
    if m <= 0 or n <= 0:
            return 0

    dp = [[0 for _ in range(n)] for _ in range(m)]

    for row in range(m):
        for col in range(n):
            if row == 0 or col == 0:
                dp[row][col] = 1
            else:
                dp[row][col] = dp[row-1][col] + dp[row][col-1]

    return dp[m-1][n-1]

# 5. Unique Paths II (Leetcode 63) 带障碍物的 Unique Paths

def uniquePathsWithObstacles(obstacleGrid):
    if not obstacleGrid:
        return 0
    
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])
    
    dp = [[0 for _ in range(n)] for _ in range(m)]

    for row in range(m):
        for col in range(n):
            if row == 0 or col == 0:
                dp[row][col] = 1
            elif obstacleGrid[row][col] == 1:
                dp[row][col] = 0
            else:
                dp[row][col] = dp[row-1][col] + dp[row][col-1]
        
    return dp[m-1][n-1]

# 6. Unique Binary Search Tree (Leetcode 96) 独一无二的BST

def numTrees(n):
    if n <= 2:
        return n

    dp = [0 for _ in range(n+1)]
    dp[:3] = [1,1,2]
    for i in range(3,n+1):
        total = 0
        for j in range(1,i+1): # 对于每个 n 来说
            total += dp[j-1] * dp[i-j] # 我们都可以让 1-n 的任何一个数当作root

        dp[i] = total
   
    return dp[-1]

# 7.  Unique Binary Search Trees II (Leetcode 95)  

def generateTrees_topdown(n):
    def genTrees(start, end, memo):
        if start > end:
            return [None]
        
        ret_list = []
        if (start, end) in memo:
            return memo[(start,end)]
        for i in range(start, end+1):
            left_subtrees = genTrees(start,i-1,memo)
            right_subtrees = genTrees(i+1, end, memo)
            for l in left_subtrees:
                for r in right_subtrees:
                    root = TreeNode(i)
                    root.left = l
                    root.right = r
                    ret_list.append(root)
        memo[(start,end)] = ret_list
        return ret_list
    if n == 0:
        return []
    else:
        return genTrees(1,n,{})

# 8. Maximum Product Subarray (Leetcode 152)  最大乘积子序列 五星
# 核心思想就是 乘法最大只有三种情况： 自己最大， 自己和前面最小值相乘最大， 自己和前面最大值相乘最大
def maxProduct(nums):
    if not nums:
        return 0
    max_dp = nums[0]
    min_dp = nums[0]
    max_sofar = max_dp

    for n in nums[1:]:
        temp = max_dp 
        max_dp = max(n, n * temp, n * min_dp)
        min_dp = max(n, n * temp, n * min_dp)
        max_sofar = max(max_dp, max_sofar)
    
    return max_sofar

# 9. Product of Array Except Self (Leetcode 238)
# O(n) Time, O(1) Space, without division
# 核心思想是 不乘某一个数字 = 它的左边乘积 * 它的右边乘积
def productExceptSelf(nums):
    if not nums:
        return []

    N = len(nums)
    output = [0] * N

    leftProduct = [1] * N
    rightProduct = [1] * N

    for i in range(1,N):
        leftProduct[i] = leftProduct[i-1] * nums[i-1]
    
    for i in range(N-2, -1, -1):
        rightProduct[i] = rightProduct[i+1] * nums[i+1]
    
    for i in range(N):
        output[i] = leftProduct[i] * rightProduct[i]
    
    return output

# 10. Different Ways to Add Parentheses


# 11. House Robber (Leetcode 198)

def rob(nums):
    if not nums:
        return 0
    if len(nums) <= 2:
        return max(nums)

    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2, len(nums)):
        dp[i] = max(nums[i] + dp[i-2], dp[i-1])
    return max(dp[-2:])

# 13. House Robber III (Leetcode 337)
def rob3(nums):
    if not nums:
        return 0
    
    

if __name__ == "__main__":
    print(rob([2,1,1,2]))