class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Use a dictionary to store the values of s in it with the amount of keys in it

        then we'll traverse the second string and see if the letter is inside the dictionary.
        if they're both empty, then we'll return True
        """
        if len(s) != len(t):
            return False

        counts = {}

        for ch in s:
            counts[ch] = counts.get(ch, 0) + 1

        for ch in t:
            if ch not in counts:
                return False
            counts[ch] -= 1
            if counts[ch] < 0:
                return False

        return True 

        

