class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        ret = 0
        for i in range(len(columnTitle)):
            ret = ret*26 + alpha.index(columnTitle[i])+1
        return ret
            