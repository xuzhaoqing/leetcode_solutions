class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        if not slots1 or not slots2:
            return []
        
        slots1.sort(key = lambda x: x[0])
        slots2.sort(key = lambda x: x[0])
        i = j = 0
        
        while i < len(slots1) and j < len(slots2):
            head = max(slots1[i][0],slots2[j][0])
            tail = min(slots1[i][1],slots2[j][1])
            
            if tail - head >= duration:
                return [head,head+duration]
            
            if tail == slots1[i][1]:
                i += 1
            else:
                j += 1
        return []
        