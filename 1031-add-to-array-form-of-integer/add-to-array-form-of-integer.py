class Solution(object):
    def addToArrayForm(self, num, k):
        n=len(num)
        digit=0
        for i in range(0,n):
            digit=digit*10+num[i]
        digit+=k
        arr=[int(d) for d in str(digit)]
        return arr
        