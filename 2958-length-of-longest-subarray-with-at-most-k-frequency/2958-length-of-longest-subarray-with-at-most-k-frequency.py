from collections import Counter 
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        ret, f = 0, -1
        count = Counter()
        for l in range(len(nums)):
            count[nums[l]] += 1
            while count[nums[l]] > k:
                f += 1
                count[nums[f]] -= 1
            ret = max(ret, l - f)
        return ret
                
                
        
        