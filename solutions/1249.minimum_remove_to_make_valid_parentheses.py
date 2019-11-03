class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        red = set()
        for i,c in enumerate(s):
            if c =='(':
                stack.append((i,c))
            elif c == ')':
                if stack and stack[-1][1] == '(':
                    stack.pop()
                else:
                    red.add(i)
        
        for i,c in stack:
            red.add(i)
            
        return ''.join([c for i,c in enumerate(s) if i not in red])