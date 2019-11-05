#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#
# https://leetcode.com/problems/koko-eating-bananas/description/
#
# algorithms
# Medium (46.97%)
# Likes:    410
# Dislikes: 44
# Total Accepted:    20.6K
# Total Submissions: 42.9K
# Testcase Example:  '[3,6,7,11]\n8'
#
# Koko loves to eat bananas.  There are N piles of bananas, the i-th pile has
# piles[i] bananas.  The guards have gone and will come back in H hours.
# 
# Koko can decide her bananas-per-hour eating speed of K.  Each hour, she
# chooses some pile of bananas, and eats K bananas from that pile.  If the pile
# has less than K bananas, she eats all of them instead, and won't eat any more
# bananas during this hour.
# 
# Koko likes to eat slowly, but still wants to finish eating all the bananas
# before the guards come back.
# 
# Return the minimum integer K such that she can eat all the bananas within H
# hours.
# 
# 
# 
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: piles = [3,6,7,11], H = 8
# Output: 4
# 
# 
# 
# Example 2:
# 
# 
# Input: piles = [30,11,23,4,20], H = 5
# Output: 30
# 
# 
# 
# Example 3:
# 
# 
# Input: piles = [30,11,23,4,20], H = 6
# Output: 23
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= piles.length <= 10^4
# piles.length <= H <= 10^9
# 1 <= piles[i] <= 10^9
# 
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        low, high = 1, max(piles)

        while low < high:
            mid = (low + high) >> 1
            hours = sum([(x+mid-1)//mid for x in piles])
            if hours > H:
                low = mid + 1
            else:
                high = mid
        return low

        
# @lc code=end

