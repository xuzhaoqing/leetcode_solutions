


# 1. Insertion Sort
def insertionSort(nums):
    for i in range(1,len(nums)):
        curNum = nums[i]
        j = i
        while j > 0 and curNum < nums[j-1]:
            nums[j] = nums[j-1]
            j -= 1
        nums[j] = curNum

# 2. Bubble Sort
def bubbleSort(nums):
    for i in range(len(nums)):
        changed = False
        for j in range(1,len(nums)-i):
            if nums[j] < nums[j-1]:
                nums[j],nums[j-1] = nums[j-1], nums[j]
                changed = True
        if not changed:
            break


# 4. Counting Sort
def countingSort(nums):
    A = nums
    