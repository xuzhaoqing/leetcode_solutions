# 一个数字，求所有位数的乘积减去所有位数的和 quora

def test(n):
    multi = 1
    total = 0

    while n >= 1:
        x = n % 10
        n = n // 10
        multi *= x
        total += x
    return multi - total

