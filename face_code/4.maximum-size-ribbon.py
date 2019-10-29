# Maximum size of ribbon

def maximumRibbon(A,k):
    if not A or k <= 0:
        return 0

    
    low, high = 1, max(A)

    while low < high:
        mid = (low + high) >> 1
        size = sum([a// mid for a in A])
        if mid <= size:
            low = mid + 1
        else:
            high = mid - 1
    
    return low - 1

if __name__ == "__main__":
    A = [1, 2, 3, 4, 9]
    k = 5
    print(maximumRibbon(A,k))