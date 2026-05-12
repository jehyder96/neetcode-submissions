class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        brute force:
        sort s and sort t
        if s and t == then return true

        also, if len(s) != len(t): return false
        """
        if len(s) != len(t):
            return False
        if sorted(s) != sorted(t):
            return False
        return True
        

