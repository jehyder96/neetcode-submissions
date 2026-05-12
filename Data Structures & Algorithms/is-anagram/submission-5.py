class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        dict = {}

        for letter in s:
            if letter in dict:
                dict[letter] += 1
            else:
                dict[letter] = 1
        
        for char in t:
            if char not in dict:
                return False
            dict[char] -= 1
            if dict[char] < 0: #for situations like s = abc t = abs
                return False
        return True