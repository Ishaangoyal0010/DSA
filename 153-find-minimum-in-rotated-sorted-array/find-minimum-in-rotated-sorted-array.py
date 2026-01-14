class Solution(object):
    def findMin(self, nums):
        n=len(nums)
        s=0
        e=n-1
        minn=float('inf')
        while s<=e:
            mid=(s+e)//2

            if nums[mid]<=nums[e]:
                minn=min(nums[mid],minn)
                e=mid-1
            else:
                minn=min(nums[s],minn)
                s=mid+1
        return minn

