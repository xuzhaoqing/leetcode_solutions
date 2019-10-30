# 1201. Ugly Number III
# Write a program to find the n-th ugly number.
# Ugly numbers are positive integers which are divisible by a or b or c.


from fractions import gcd
def nthUglyNumber(n, a, b ,c ):
    def lcm(a,b):
        return a * b // gcd(a,b)
    def lcm3(a,b,c):
        return a * b * c // gcd(a,gcd(b,c))
    
    def f(x):
        return x // a + x // b + x // c - x // lcm(a,b) - x // lcm(b,c) - \
                x // lcm(a,c) + x // lcm3(a,b,c)

    low,high = 0, 2*10**9

    while low < high:
        mid = (low + high) >> 1
        if f(mid) >= n:
            high = mid
        else:
            low = mid + 1
    return low