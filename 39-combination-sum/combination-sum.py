class Solution(object):
    def backtrack(self, index,nums, subset,total,result,target):
        if total==target:
            result.append(list(subset))            
            return
        if index>=len(nums):
            return 
        if total>target:
            return
        summ=total+nums[index]
        subset.append(nums[index])
        self.backtrack(index,nums,subset,summ,result,target)
        subset.pop()
        summ=total
        self.backtrack(index+1,nums,subset,summ,result,target)

    def combinationSum(self, candidates, target):
        result=[]
        self.backtrack(0,candidates,[],0,result,target)
        return result
        