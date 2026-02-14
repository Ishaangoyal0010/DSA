class Solution(object):
    def majorityElement(self, nums):
        n=len(nums)
        can=nums[0]
        vote=0
        for i in range(n):
            if vote ==0:
                can=nums[i]
                vote+=1
            elif nums[i]==can:
                vote+=1
            else:
                vote-=1
        return can

        