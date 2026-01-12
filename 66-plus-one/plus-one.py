class Solution(object):
    def plusOne(self, digits):
        num=0
        n= len(digits)
        for i in range(0,n):
            num=num*10+digits[i]
        num+=1
        arr = [int(d) for d in str(num)]

        return arr


        