from basicDS import TreeNode, ListNode

#1 Convert Sorted Array to Binary Search Tree (Leetcode 108)
def sortedArrayToBST(nums):
    if not nums:
        return None
    
    mid = len(nums) // 2
    node = TreeNode(nums[mid])
    node.left = sortedArrayToBST(nums[:mid])
    node.right = sortedArrayToBST(nums[mid+1:])
    return node


#2 Convert Sorted Linked List to Binary Search Tree (Leetcode 109)
def sortedListToBST1(head):
        # 递归版本， 首先利用快慢指针找到中间值，然后递归调用左右的子树
        if not head:
            return head
        
        prevPtr = None
        slowPtr = head
        fastPtr = head
        while fastPtr and fastPtr.next:
            prevPtr = slowPtr
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next.next
        
        if prevPtr:
            prevPtr.next = None
        
        root = TreeNode(slowPtr.val)
        
        if slowPtr == head: # 这步很重要，否则几乎是无限递归
            return root
        
        root.left = sortedListToBST1(head)
        root.right = sortedListToBST1(slowPtr.next)
        
        return root

def sortedListToBST2(head):
    # 将链表转换成数组，再调用第一个方法，时间复杂度为O(N)
    array = []
    while head:
        array.append(head.val)
        head = head.next
    
    return sortedArrayToBST(array)


def sortedListToBST3(head):
    # 有点难，没看懂
    pass


