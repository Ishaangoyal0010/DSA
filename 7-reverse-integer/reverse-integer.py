class Solution(object):
    def reverse(self,x):
        sign = -1 if x < 0 else 1
        reversed_num = int(str(abs(x))[::-1]) * sign
        return reversed_num if -2**31 <= reversed_num < 2**31 else 0
        