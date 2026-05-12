from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        maybe we can add s & t together and see is is inside the joint string?
        """
        # Normalize the strings
        # Normalize the strings
        str1 = s.replace(" ", "")
        str2 = t.replace(" ", "")
    
        # Use Counter to count character frequencies
        return Counter(str1) == Counter(str2)