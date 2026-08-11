class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        n = nums[0]
        i = 1
        while i<len(nums):
            if nums[i] != nums[i-1] + 1:
                break
            n,i = nums[i]+n, i+1
        s = set(nums)
        while n in s:
            n += 1
        return n

            
