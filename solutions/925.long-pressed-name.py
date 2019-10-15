#
# @lc app=leetcode id=925 lang=python3
#
# [925] Long Pressed Name
#
# https://leetcode.com/problems/long-pressed-name/description/
#
# algorithms
# Easy (44.58%)
# Likes:    294
# Dislikes: 40
# Total Accepted:    21.9K
# Total Submissions: 49.2K
# Testcase Example:  '"alex"\n"aaleex"'
#
# Your friend is typing his name into a keyboard.  Sometimes, when typing a
# character c, the key might get long pressed, and the character will be typed
# 1 or more times.
# 
# You examine the typed characters of the keyboard.  Return True if it is
# possible that it was your friends name, with some characters (possibly none)
# being long pressed.
# 
# 
# 
# Example 1:
# 
# 
# Input: name = "alex", typed = "aaleex"
# Output: true
# Explanation: 'a' and 'e' in 'alex' were long pressed.
# 
# 
# 
# Example 2:
# 
# 
# Input: name = "saeed", typed = "ssaaedd"
# Output: false
# Explanation: 'e' must have been pressed twice, but it wasn't in the typed
# output.
# 
# 
# 
# Example 3:
# 
# 
# Input: name = "leelee", typed = "lleeelee"
# Output: true
# 
# 
# 
# Example 4:
# 
# 
# Input: name = "laiden", typed = "laiden"
# Output: true
# Explanation: It's not necessary to long press any character.
# 
# 
# 
# 
# 
# 
# 
# Note:
# 
# 
# name.length <= 1000
# typed.length <= 1000
# The characters of name and typed are lowercase letters.
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if len(typed) < len(name):
            return False
    
        pn, pt = 0,0 
        
        while pn < len(name):
            if name[pn] == typed[pt]:
                pn += 1
                pt += 1
            else:
                pt += 1
            print(pn,pt)
            if pt >= len(typed) and pn < len(name):
                return False
        return True
# @lc code=end

if __name__ == "__main__":
    s = Solution()
    name = "saeed"
    typed = "ssaaedd"
    print(s.isLongPressedName(name,typed))
