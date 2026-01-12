class Solution(object):
    #done
    def longestConsecutive(self, nums):
       n=len(nums)
       nums.sort()
       maxi=1
       cnt=1
       if n ==0:
        return 0
       for i in range(1,n):
            if nums[i]==nums[i-1]:
                continue
            elif nums[i]==nums[i-1]+1:
                cnt+=1
            else:
                maxi=max(maxi,cnt)
                cnt=1
       return max(maxi,cnt)