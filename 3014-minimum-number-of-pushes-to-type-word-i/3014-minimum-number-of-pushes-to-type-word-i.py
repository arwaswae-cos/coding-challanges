class Solution:
    def minimumPushes(self, word: str) -> int:
        size = len(word)
        p = ((size-1)//8) + 1
        pushes = (p*(p-1)*4) + (size-(p-1)*8)*p
        return pushes
