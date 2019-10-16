class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        # Edit Sentence 的简易版本，但是前三个if else很烦人
        def dp(i,j,choice):
            if i == len(s) and j == len(t):
                return choice == 0
            if i == len(s):
                return choice == 1 and len(t) - j == 1
            if j == len(t):
                return choice == 1 and len(s) - i == 1
            
            if s[i] == t[j]:
                return dp(i+1,j+1,choice)
            elif not choice:
                return False
            else:
                insert = dp(i,j+1,choice-1)
                delete = dp(i+1,j,choice-1)
                replace = dp(i+1,j+1,choice-1)
                return insert or delete or replace
        return dp(0,0,1)