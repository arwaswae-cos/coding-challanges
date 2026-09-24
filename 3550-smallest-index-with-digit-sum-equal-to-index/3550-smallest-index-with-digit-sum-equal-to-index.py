class Solution:
    def findSum(self, num):
        return sum(list(map(int,str(num))))
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if self.findSum(nums[i]) == i:
                return i
        return -1
        