# coding=utf-8
"""
This file is about the code snippets I wrote for dynamic programming algorithmic problems
"""

from basicDS import ListNode

# 1. Reverse Linked List  翻转链表

def reverse_linked_list_iter(head: ListNode) -> ListNode:  # 迭代版
    cur = head
    while cur and cur.next:
        temp = cur.next
        cur.next = temp.next
        temp.next = head
        head = temp
    return head

def reverse_linked_list_rev(head: ListNode) -> ListNode: # 递归版
    if not (head and head.next):
            return head
    p = self.reverseList(head.next)
    head.next.next = head
    head.next = None
    return p

# 2. Check if a linked list is palindrome  # 链表回文
#  将后半段翻转，check完之后再翻转回去
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not (head and head.next):
            return True
        
        count = 0
        p = head
        while p:
            count += 1
            p = p.next
        
        is_even = (count % 2) == 0
        if is_even:
            reverseStartIndex = count // 2
        else:
            reverseStartIndex = count // 2 + 1
        
        secondHalf = head
        for _ in range(reverseStartIndex):
            secondHalf = secondHalf.next
        
        firstHalf = head
        secondHalf = self.reverseLinkedList(secondHalf)
        secondHalfStart = secondHalf
        while secondHalf.next:
            if firstHalf.val != secondHalf.val:
                return False
            firstHalf = firstHalf.next
            secondHalf = secondHalf.next
        
        if firstHalf.val != secondHalf.val:
            return False
        
        if is_even:
            firstHalf.next = self.reverseLinkedList(secondHalfStart)
        else:
            firstHalf.next.next = self.reverseLinkedList(secondHalfStart)
        printLinkedList(head)
        return True
        
    
    def reverseLinkedList(self,head):
        cur = head
        
        while cur and cur.next:
            temp = cur.next
            cur.next = temp.next
            temp.next = head
            head = temp
        return head


# helper functions for runnning these functions
def listToLinkedList(l):
    if not l:
        return None
    head = ListNode(l[0])
    cur = head
    for val in l[1:]:
        node = ListNode(val)
        cur.next = node
        cur = node
    return head

def printLinkedList(head):
    if not head:
        print('None')
        return 
    print(head.val,end=' ')
    head = head.next
    while head:
        print(' ->',end=' ')
        print(head.val, end = ' ')
        head = head.next
    print()

if __name__ == "__main__":
    q = [1,2,3,3,2,1]
    print(Solution().isPalindrome(listToLinkedList(q)))
