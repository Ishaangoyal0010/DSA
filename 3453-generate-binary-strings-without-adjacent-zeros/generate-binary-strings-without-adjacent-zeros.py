class Solution(object):
    def backtrack(self,index,number,flag,result):
        if index>=len(number):
            result.append(''.join(number))
            return
        if flag==False:
            number[index]='0'
            self.backtrack(index+1,number,True,result)
        number[index]='1'
        self.backtrack(index+1,number,False,result)


    def validStrings(self, n):
        number=[1]*n
        result=[]
        self.backtrack(0,number,False,result)
        return result
        