class Solution(object):
    def search(self, nums, target):
        n= len(nums)
        s=0
        e=n-1
        while s<=e:
            mid=(s+e)//2
            if nums[mid]==target:
                return True
            if nums[mid]==nums[e]==nums[s]:
                s+=1
                e-=1
                continue
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
        return False