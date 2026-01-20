class Solution(object):
    def search(self, nums, target):
        s=0
        n=len(nums)
        e=n-1
        mid=(s+e)//2
        while s<=e:
            if nums[mid]==target:
                return mid
            if nums[mid]<target:
                s=mid+1
            else:
                e=mid-1
            mid=(s+e)//2
        return -1
        