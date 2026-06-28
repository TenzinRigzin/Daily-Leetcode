class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        result=nums1+nums2
        result.sort()
        size=len(result)

        if(size%2==0):
            ans1=result[(size//2)-1]
            ans2=result[size//2]
            ans=(ans1+ans2)/2   
        else:
            ans=result[size//2]
        return ans

