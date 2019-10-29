# https://leetcode.com/discuss/interview-question/352458/Google-or-OA-2019-or-Compare-Strings


def compareString(A,B):
    if not A or not B:
        return []

    
    freq = [0] * 11
    A, B = A.split(','), B.split(',')
    C = [0] * len(B)
    for word in A:
        freq[word.count(min(word))] += 1
    
    for i,word in enumerate(B):
        f = word.count(min(word))
        C[i] = sum(freq[:f])
    return C

print(compareString("",""))
print(compareString("a",""))
print(compareString("a","aba"))
print(compareString("",""))