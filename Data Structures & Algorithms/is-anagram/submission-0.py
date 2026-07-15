class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars = dict()
        for i in s:
            if i not in chars:
                chars[i]=0
            else:
                chars[i]=chars[i]+1
        chart = dict()
        for i in t:
            if i not in chart:
                chart[i]=0
            else:
                chart[i]=chart[i]+1
        if chars == chart:
            return True
        else:
            return False