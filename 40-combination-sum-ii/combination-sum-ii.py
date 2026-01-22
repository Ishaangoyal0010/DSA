class Solution(object):
    def backtrack(self,candidates, target,index,subset,total,result):
        if total==target:
            result.append(list(subset))
            return
        if index>=len(candidates):
            return
        if total>target:
            return
        for i in range(index,len(candidates)):
            if i>index and candidates[i]==candidates[i-1]:
                continue
            subset.append(candidates[i])
            summ=total+candidates[i]
            self.backtrack(candidates, target,i+1,subset,summ,result)
            subset.pop()


    def combinationSum2(self, candidates, target):
        candidates.sort()
        result=[]
        self.backtrack(candidates, target,0,[],0,result)
        return result
        