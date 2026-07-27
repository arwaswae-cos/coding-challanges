class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxx,second_maxx = -1,-1
        for i in range(len(nums)):
            if nums[i] >= maxx:
                second_maxx,maxx = maxx,nums[i]
            elif nums[i] > second_maxx:
                second_maxx = nums[i]
        return (maxx-1)*(second_maxx-1)
                
            

        