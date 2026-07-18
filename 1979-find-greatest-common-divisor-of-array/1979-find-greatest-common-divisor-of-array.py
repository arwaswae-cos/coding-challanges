import math as m
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        return m.gcd(min(nums),max(nums))

        