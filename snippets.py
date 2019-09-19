from basicDS import TreeNode, ListNode
# 1. Reverse Linked List  翻转链表
def reverse_linked_list_iter(head: ListNode) -> ListNode:  # 迭代版
    cur = head
    while cur and cur.next:
        temp = cur.next
        cur.next = temp.next
        temp.next = head
        head = temp
    return head
# 2. Slow Pointer and Fast Pointer 快慢指针
# This is often used in finding the middle node of the linked list
#                   or checking if the graph is cyclic
def find_middle_node(head):
    slowPtr = head
    fastPtr = head
    while fastPtr and fastPtr.next:
        slowPtr = slowPtr.next
        fastPtr = fastPtr.next.next

    return slowPtr



