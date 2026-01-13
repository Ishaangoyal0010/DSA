class Solution(object):
    def searchRange(self, nums, target):
        s = -1
        e = -1
        n = len(nums)
        for i in range(0,n):
            if nums[i]==target:
                if s==-1:
                    s=i
                e=i

        return [s,e]
