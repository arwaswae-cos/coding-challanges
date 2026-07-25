class Solution:
    def maxProduct(self, n: int) -> int:
        maxx = 0
        n = list(map(int, str(n)))
        l = len(n)
        for i in range(l):
            s = n[i]
            for j in range(i+1,l):
                pro = s*n[j]
                if pro > maxx:
                    maxx = pro
        return maxx

        