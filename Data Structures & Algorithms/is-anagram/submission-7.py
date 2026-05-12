class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        brute force:
        sort s and sort t
        if sorted(s) != sorted(t):
            return False
        return True
        """
        """
        Plan:
    If len(s) != len(t), return False early.
    Count how many times each character appears in s.
    Decrement the count for each character in t.
    If any count goes negative or a char in t isn’t in the map → not an anagram.
    If all counts are zero at the end → it’s an anagram.
     
        """
        if len(s) != len(t):
            return False

        anagram = {}

        for letter in s:
            if letter in anagram:
                anagram[letter] += 1
            else:
                anagram[letter] = 1
        
        for letter in t:
            if letter not in anagram:
                return False
            if letter in anagram:
                anagram[letter] -= 1
            if anagram[letter] < 0:
                return False
        return True
        

