class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        lst = []
        for i in ransomNote:
            if i not in lst:
                if magazine.count(i) < ransomNote.count(i):
                    return False
                lst.append(i)
        return True