class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:

        min_sum = 9999999999999
        for left in range(len(nums)):                                             
            
            for right in range(left,len(nums)):      
                
                if l<=len(nums[left:right+1]) and len(nums[left:right+1])<=r and sum(nums[left:right+1])>0:

                    list_sum = sum(nums[left:right+1])                   
                    min_sum = min(min_sum,list_sum)                
        if min_sum == 9999999999999:
            return -1

        if min_sum<0:
            return -1
        return min_sum

        #left = 
        #right 
        #min_sum = 9999999999999,