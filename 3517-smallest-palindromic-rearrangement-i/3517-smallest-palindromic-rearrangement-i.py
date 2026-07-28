from collections import Counter 
class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n = Counter(s)
        k = sorted(list(n.keys()))
        frnt,bck = '',''
        mid = ''
        for _ in k:
            t = n[_]//2 if n[_]>1 else 0
            frnt += _*t
            bck = _*t + bck
            n[_] -= 2*t
            if n[_]%2 != 0:
                mid += _
        return frnt+mid+bck
        