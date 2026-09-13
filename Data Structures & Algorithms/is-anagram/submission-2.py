class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        length = len(s)
        char1 = {}
        char2 = {}

        if len(s) != len(t):
            return False
        
        for i in range(length):
            if s[i] in char1:
                char1[s[i]] += 1
            else:
                char1[s[i]] = 0 
            
            if t[i] in char2:
                char2[t[i]] += 1
            else:
                char2[t[i]] = 0 

        return char1 == char2
            