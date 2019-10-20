from collections import defaultdict
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        visited = set()
        folder.sort(key = lambda x: x.count('/'))
        ret = []
        for m in folder:
            d = m.split('/')[1:]
            name = d[-1] + str(len(d))
            d = d[:-1]
            found = False
            for i,x in enumerate(d,1):
                if x+str(i) in visited:
                    found = True
                    break
            
            if  not found:
                visited.add(name)
                ret.append(m)
        return ret