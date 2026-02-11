class Solution(object):
    def twoSum(self, nums, target):
        # Dictionary to store value -> index
        seen = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            
            # Check if complement exists in our dictionary
            if complement in seen:
                return [seen[complement], i]
            
            # Store current number and its index
            seen[num] = i
 