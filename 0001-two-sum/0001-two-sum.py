class Solution(object):
    def twoSum(self, nums, target):
        list1=[]
        for i in range(0,len(nums)):
            num1=nums[i]
            for j in range(i+1,len(nums)):
                num2=nums[j]
                if num1+num2==target:
                    list1.append(i)
                    list1.append(j)
                    return list1
                    