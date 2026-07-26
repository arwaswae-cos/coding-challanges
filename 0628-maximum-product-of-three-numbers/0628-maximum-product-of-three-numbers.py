class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        ret1 = nums[-1]*nums[-2]*nums[-3]
        ret2 = nums[0]*nums[1]*nums[-1]
        return max(ret1,ret2)