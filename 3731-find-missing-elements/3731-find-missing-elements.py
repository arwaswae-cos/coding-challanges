class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        minn, maxx = min(nums), max(nums)
        s = set(nums)
        ret = [i for i in range(minn+1,maxx) if i not in s]
        return ret