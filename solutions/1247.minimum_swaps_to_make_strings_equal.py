#1

class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        x, y = 0, 0
        if len(s1) != len(s2):
            return -1
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if s1[i] == 'x':
                    x += 1
                else:
                    y += 1
        if (x+y) % 2 == 1:
            return -1
        
        return x // 2 + y // 2 + 2 * ( x % 2 )
        