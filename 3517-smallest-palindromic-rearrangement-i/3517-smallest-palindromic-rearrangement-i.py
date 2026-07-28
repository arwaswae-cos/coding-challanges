from collections import Counter 
class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n = Counter(s)
        k = sorted(list(n.keys()))
        frnt = ''
        mid = ''
        for _ in k:
            t = n[_]//2 
            frnt += _*t
            n[_] -= 2*t
            if n[_]%2 != 0:
                mid += _
        return frnt+mid+frnt[::-1]
        