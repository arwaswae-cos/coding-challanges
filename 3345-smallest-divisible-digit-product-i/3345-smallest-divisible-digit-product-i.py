class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        s = list(map(int,str(n)))
        pr = 1
        for i in s:
            pr *= i
        if pr%t == 0:
            return n
        return self.smallestNumber(n+1, t)

        
        