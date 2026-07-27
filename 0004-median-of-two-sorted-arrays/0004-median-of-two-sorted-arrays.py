class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num = nums1+nums2
        num.sort()
        mid=len(num)//2
        return num[mid] if len(num)%2 != 0 else (num[mid]+num[mid-1])/2