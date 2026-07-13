class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = nums1 + nums2
        nums3.sort()
        if len(nums3) % 2 != 0:
            b=len(nums3)//2
            return nums3[b]
        else:
            b=((len(nums3))+1)//2 
            c=((len(nums3))-1)//2 
            d=(nums3[b]+nums3[c])/2
            return d