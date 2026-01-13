class Solution(object):
    def search(self, nums, target):
        s=-1
        n= len(nums)
        for i in range(0,n):
            if nums[i]==target:
                s=i
        return s
        