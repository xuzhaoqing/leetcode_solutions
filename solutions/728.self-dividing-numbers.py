#
# @lc app=leetcode id=728 lang=python3
#
# [728] Self Dividing Numbers
#
# https://leetcode.com/problems/self-dividing-numbers/description/
#
# algorithms
# Easy (71.43%)
# Likes:    472
# Dislikes: 256
# Total Accepted:    95.2K
# Total Submissions: 133.1K
# Testcase Example:  '1\n22'
#
# 
# A self-dividing number is a number that is divisible by every digit it
# contains.
# 
# For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 ==
# 0, and 128 % 8 == 0.
# 
# Also, a self-dividing number is not allowed to contain the digit zero.
# 
# Given a lower and upper number bound, output a list of every possible self
# dividing number, including the bounds if possible.
# 
# Example 1:
# 
# Input: 
# left = 1, right = 22
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
# 
# 
# 
# Note:
# The boundaries of each input argument are 1 .
# 
#

# @lc code=start
class Solution:
    def selfDividingNumbers(self, left: int, right: int):
        ret = []
        for num in range(left, right+1):
            n = num
            tens = 10
            digit = n % tens
            while n > 0 and digit > 0 and num % digit == 0:
                n /= 10
                digit = n % tens
            print(num,n)
            if n == 0:
                ret.append(num)
        return ret
        
# @lc code=end
if __name__ == "__main__":
    s = Solution()  
    print(s.selfDividingNumbers(1,22))
