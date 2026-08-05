import sys
sys.set_int_max_str_digits(10000)
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        n, length = 0, len(num)
        for i in range(length):
            n = n*10 + num[i]
        return list(map(int, str(n+k)))