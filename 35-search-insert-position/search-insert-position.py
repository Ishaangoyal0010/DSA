class Solution(object):
    def searchInsert(self, nums, target):
        n=len(nums)
        if target<=nums[0]:
                return 0
        if target>nums[n-1]:
            return n
        for i in range(0,n-1):
            if nums[i]<target and nums[i+1]>=target:
                return i+1

            

        