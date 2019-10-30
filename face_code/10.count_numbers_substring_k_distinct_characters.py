# Given a string of lowercase alphabets, count all possible substrings (not necessarily distinct) that has exactly k distinct characters.
from collections import deque
def countDist(s, k):
    table = [0] * 26
    if len(s) < k:
        return 0
    q = deque(s[:k])
    for i in range(k):
        table[ord(s[i])-ord('a')] += 1
    count = distinct(table)
    i = k
    while i < len(s):
        poped = q.popleft()
        table[ord(poped) - ord('a')] -= 1
        table[ord(s[i]) - ord('a')] += 1
        q.append(s[i])
        count += distinct(table)
        i += 1
    return count

def distinct(table):
    for i in table:
        if i > 1:
            return False
    return True

if __name__ == "__main__":
    print(countDist('abcbaa',3))