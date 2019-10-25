# n个人围成一个圈，编号1-n,给定整数k，数到k时对应的人淘汰，从下一个人开始计数,输出被淘汰的人的
# 编号的list

def roundCount(n,k):
    l = list(range(1,n+1))
    pos = 0
    ret = []
    while l:
        index = (pos + k - 1) % len(l)
        ret.append(l[index])
        l = l[:index] + l[index+1:]
        pos = index
    return ret


n,k = 5, 3
print(roundCount(5,3))