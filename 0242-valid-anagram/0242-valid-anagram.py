class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        lst = []
        for i in t:
            if i not in lst:
                if s.count(i) != t.count(i):
                    return False
                lst.append(i)
        return True