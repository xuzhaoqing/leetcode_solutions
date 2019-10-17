#
# @lc app=leetcode id=220 lang=python3
#
# [220] Contains Duplicate III
#
# https://leetcode.com/problems/contains-duplicate-iii/description/
#
# algorithms
# Medium (20.11%)
# Likes:    788
# Dislikes: 790
# Total Accepted:    103.2K
# Total Submissions: 510.5K
# Testcase Example:  '[1,2,3,1]\n3\n0'
#
# Given an array of integers, find out whether there are two distinct indices i
# and j in the array such that the absolute difference between nums[i] and
# nums[j] is at most t and the absolute difference between i and j is at most
# k.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,2,3,1], k = 3, t = 0
# Output: true
# 
# 
# 
# Example 2:
# 
# 
# Input: nums = [1,0,1,1], k = 1, t = 2
# Output: true
# 
# 
# 
# Example 3:
# 
# 
# Input: nums = [1,5,9,1,5,9], k = 2, t = 3
# Output: false
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k: int, t: int) -> bool:

        if t==0 and len(nums)== len(set(nums)): 
            return False
        for i in range(len(nums)):
            for j in range(1,k+1):
                if i+j >= len(nums):
                    break
                if abs(nums[i+j]-nums[i])<=t:
                    return True
        return False
            


        # if not nums or k < 0 or t < 0:
        #     return False

        # hashTable, visited = {}, set()
        # for i,n in enumerate(nums):
        #     visited.add(n)
        #     if n in hashTable and abs(hashTable[n] - i) <= k:
        #         return True
        #     hashTable[n] = i

        #     if len(visited) < 2*t:
        #         for h in visited:
        #             if h in range(n-t,n+t+1) and h != n and h in hashTable and abs(hashTable[h] - hashTable[n]) <= k:
        #                 return True
        #     else:
        #         for h in range(n-t,n+t+1):
        #             if h in visited and h != n and h in hashTable and abs(hashTable[h]-hashTable[n]) <= k:
        #                 return True
        # return False
# @lc code=end

if __name__ == "__main__":
    s = Solution()
#     nums = [1,5,9,1,5,9]
#     k,t = 2,3
    nums = [2,1]
    k,t = 1,1 
    print(s.containsNearbyAlmostDuplicate(nums,k,t))