# Given a string of lowercase alphabets, count all possible substrings (not necessarily distinct) that has exactly k distinct characters.



def countDist(s,k):
    if k <= 0 or len(s) < k:
        return []
    ret = []
    for i in range(len(s)-k+1):
        if len(set(s[i:i+k])) == k and s[i:i+k] not in ret:
            ret.append(s[i:i+k])
    return ret




#from collections import deque
# def countDist(s, k):
#     table = [0] * 26
#     if len(s) < k:
#         return 0
#     q = deque(s[:k])
#     for i in range(k):
#         table[ord(s[i])-ord('a')] += 1

#     ret = []
#     if distinct(table) and ''.join(q) not in ret:
#         ret.append(''.join(q))
#     i = k
#     while i < len(s):
#         poped = q.popleft()
#         table[ord(poped) - ord('a')] -= 1
#         table[ord(s[i]) - ord('a')] += 1
#         q.append(s[i])
#         if distinct(table) and ''.join(q) not in ret:
#             ret.append(''.join(q))
#         i += 1
#     return ret

# def distinct(table):
#     for i in table:
#         if i > 1:
#             return False
#     return True

if __name__ == "__main__":
    print(countDist('abcabc',3))
    print(countDist(s = "awaglknagawunagwkwagl", k = 4))