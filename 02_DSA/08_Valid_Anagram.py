'''
If len(s) != len(t), return False.
countS = {}.
Loop through string s.
If the letter is already in countS, add 1 to its value.
If the letter is new, put it in with a value of 1.
Do the exact same thing for string t using a second dictionary countT = {}.
if countS == countT: return True.
'''
'''
The solution uses O(s+t time which is optimmal but there are two dictionaries)
This can be turned into one dictionary if you subtract 1 for every letter in t
if the dictionary is full of zeroes'0' it's an ANAGRAM.
'''
#Improved Solution
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count={}
        for ch in s:
            count[ch] = 1 + count.get(ch, 0)
        for ch in t:
            if ch not in count or count[ch] == 0:
                return False
            count[ch] -= 1
        return True
'''
#Basic SOLUTION
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countS={}
        countT={}
        for ch in s:
            countS[ch] = 1 + countS.get(ch, 0)
        for i in t:
            countT[ch] = 1 + countT.get(ch, 0)
        if countS == countT:
            return True
        
'''