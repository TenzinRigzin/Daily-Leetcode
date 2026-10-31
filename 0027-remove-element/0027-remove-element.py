class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        for i in range(len(nums)):
            ltemp=[]
            temp = nums.pop(0)
            if temp != val:
                nums.append(temp)
        return len(nums)
                