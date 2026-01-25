class Solution(object):
    def backtrack(self, index, subset, nums, result):
        
        result.append(list(subset))

        for i in range(index, len(nums)):
            if i>index and nums[i]==nums[i-1]:
                continue
            subset.append(nums[i])
            self.backtrack(i+1, subset, nums, result)
            subset.pop()
    def subsetsWithDup(self, nums):
        nums.sort()
        result=[]
        self.backtrack(0, [], nums, result)
        return result
        