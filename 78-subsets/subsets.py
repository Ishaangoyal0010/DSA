class Solution(object):
    def backtrack(self, index, subset, nums, result):
        if index>=len(nums):
            result.append(list(subset))
            return
        subset.append(nums[index])
        self.backtrack(index+1, subset, nums, result)
        subset.pop()
        self.backtrack(index+1, subset, nums, result)
    def subsets(self, nums):
        result=[]
        self.backtrack(0,[],nums,result)
        return result