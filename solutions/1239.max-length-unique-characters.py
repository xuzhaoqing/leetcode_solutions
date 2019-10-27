class Solution:
    def maxLength(self, arr) -> int:
        if not arr:
            return 0
        maxLen = 0
        dp = set()
        
        for word in arr:
            if len(word) != len(set(word)):
                continue
            new_dp = set(dp)
            for seg in dp:
                has = [1 for c in word if c in seg]
                if not has:
                    maxLen = max(maxLen,len(seg+word))
                    new_dp.add(seg+word)
            maxLen = max(maxLen,len(word))
            new_dp.add(word)
            dp =new_dp
        return maxLen


if __name__ == "__main__":
    s = Solution()
    arr=  ["yy","bkhwmpbiisbldzknpm"]
    print(s.maxLength(arr))