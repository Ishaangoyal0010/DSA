class Solution(object):
    def search(self, nums, target):
        s=0
        n= len(nums)
        e=n-1
       
        while s<=e:
            mid=(e+s)//2
            if nums[mid]==target:
                return mid
            if nums[e]>=nums[mid]:
                if nums[mid]<=target<=nums[e]:
                    s=mid+1
                else:
                    e=mid-1
            else:
                if nums[s]<=target<=nums[mid]:
                    e=mid-1
                else:
                    s=mid+1
                
        return -1
        