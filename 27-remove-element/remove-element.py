class Solution(object):
    def removeElement(self, nums, val):
        n=len(nums)
        s=0
        for i in range(0,n):
            if nums[i]!=val:
                nums[s],nums[i]=nums[i],nums[s]
                s+=1
        return s
            