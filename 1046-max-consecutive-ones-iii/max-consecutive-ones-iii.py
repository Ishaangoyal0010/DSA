class Solution(object):
    def longestOnes(self, nums, k):
        mapp={}
        left=0
        right=0
        maxi=0
        zeros=0
        n=len(nums)
        while right<n:
            if nums[right]==0:
                zeros+=1
            if zeros>k:
                if nums[left]==0:
                    zeros-=1
                left+=1
                
            maxi=max(maxi,right-left+1)
            right+=1
        return maxi

        