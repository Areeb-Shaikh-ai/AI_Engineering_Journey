#Leetcode Solution 392
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        while i<len(s) and j<len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)

'''
Initialize i = 0 and j = 0.
Use a while loop that runs as long as i < len(s) AND j < len(t).
Inside:
If s[i] == t[j]: move i forward.
Always move j forward (regardless of a match).

'''