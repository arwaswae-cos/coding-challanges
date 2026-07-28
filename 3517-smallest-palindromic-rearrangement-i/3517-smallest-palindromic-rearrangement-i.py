from collections import Counter 
class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n = Counter(s)
        k = sorted(list(n.keys()))
        frnt,bck = '',''
        mid = ''
        for _ in k:
            while n[_]!=0 and n[_]>1:
                frnt += _
                bck = _ + bck
                n[_] -= 2
            if n[_]%2 != 0:
                mid += _
        return frnt+mid+bck
        