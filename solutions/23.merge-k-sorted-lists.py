#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#
# https://leetcode.com/problems/merge-k-sorted-lists/description/
#
# algorithms
# Hard (36.08%)
# Likes:    3234
# Dislikes: 214
# Total Accepted:    490.2K
# Total Submissions: 1.3M
# Testcase Example:  '[[1,4,5],[1,3,4],[2,6]]'
#
# Merge k sorted linked lists and return it as one sorted list. Analyze and
# describe its complexity.
# 
# Example:
# 
# 
# Input:
# [
# 1->4->5,
# 1->3->4,
# 2->6
# ]
# Output: 1->1->2->3->4->4->5->6
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import heapq
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        h = []
        for l in lists:
            cur = l
            while cur:
                heapq.heappush(h,cur.val)
                cur = cur.next
        dummy = ListNode(0)
        cur = dummy
        while h:
            v = heapq.heappop(h)
            cur.next = ListNode(v)
            cur = cur.next
        return dummy.next

# @lc code=end

