# Given a list of positive integers nums and an int target, return indices of the two numbers such that they add up to a target - 30.

# Conditions:

# You will pick exactly 2 numbers.
# You cannot pick the same element twice.
# If you have muliple pairs, select the pair with the largest number.


def findPairs(nums, target):
    hashMap = {}
    maxNum = -1
    ret = [-1,-1]
    target -= 30

    for i,n in enumerate(nums):
        if target - n in hashMap and maxNum < max((n,target-n)):
            maxNum = max((n,target-n))
            ret = [i,hashMap[target-n]]
        hashMap[n] = i

    if maxNum == -1:
        return None
    return ret

if __name__ == "__main__":
    nums = [20, 50, 40, 25, 30, 10]
    target = 90
    print(findPairs(nums,target))
    