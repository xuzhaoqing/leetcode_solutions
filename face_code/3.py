# 输入一组 words 和一组 valid letters，判断有多少个 words 是 valid。判断条件是 words里的所有 upper and lower letter 必须在 valid letters 里面。如果 word 里面有 special character 不用管

def validWords(self, words, letters):
    letters = set(letters)
    valid = []
    for word in words:
        found = False
        for c in word:
            if 'A' <= c <= 'z':
                if c not in letters:
                    found = True
                    break
        
        if not found:
            valid.append(word)

    return valid
