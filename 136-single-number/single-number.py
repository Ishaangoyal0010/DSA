class Solution(object):
    def singleNumber(self, nums):
        n=len(nums)
        hash_map={}
        for i in range(0,n):
            if nums[i] in hash_map:
                hash_map[nums[i]]+=1
            else:
                hash_map[nums[i]]=1
        for i in hash_map:
            if hash_map[i]==1:
                return i

                
                

        