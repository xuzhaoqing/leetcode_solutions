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

# 3. Insertion Sort

def insertionSort(nums):
    for i in range(1,len(nums)):
        curNum = nums[i]
        j = i
        while j > 0 and curNum < nums[j-1]:
            nums[j] = nums[j-1]
            j -= 1
        nums[j] = curNum

# 4. Bubble Sort
def bubbleSort(nums):
    for i in range(len(nums)):
        changed = False
        for j in range(1,len(nums)-i):
            if nums[j] < nums[j-1]:
                nums[j],nums[j-1] = nums[j-1], nums[j]
                changed = True
        if not changed:
            break

# 5. Union Find
class UnionFind:
            def __init__(self,n):
                self.parents = [i for i in range(n)]
                self.ranks = [0 for i in range(n)]
                
            def find(self,x):
                if x != self.parents[x]:
                    self.parents[x] = self.find(self.parents[x]) # path compression
                
                return self.parents[x]
            
            def unite(self, x,y):
                x, y = self.find(x), self.find(y)
                if x == y:
                    return 
                if(self.ranks[x] < self.ranks[y]):
                    self.parents[x] = y
                else:
                    self.parents[y] = x
                    if (self.ranks[x] == self.ranks[y]): 
                        self.ranks[x] += 1
            def __len__(self):
                ret = 0
                for i,x in enumerate(self.parents):
                    if i == x:
                        ret += 1
                return ret

if __name__ == "__main__":
    nums = [23,434,5,67,6,23,5,47,76,21]
    bubbleSort(nums)
    print(nums)