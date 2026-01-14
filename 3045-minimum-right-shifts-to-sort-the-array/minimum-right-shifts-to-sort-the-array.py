class Solution(object):
    def minimumRightShifts(self, nums):
      n=len(nums)
      index=-1
      count=0
      maxi=float('-inf')
      if nums[-1] > nums[0]:
        count += 1
      for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            count += 1
            if count>1:
                return -1
      for i in range(0,n):
        if nums[i]>=maxi:
            maxi=nums[i]
            index=i
        
      return n-index-1