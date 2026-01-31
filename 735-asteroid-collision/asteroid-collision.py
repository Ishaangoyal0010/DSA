class Solution(object):
    def asteroidCollision(self, asteroids):
        stack=[]
        for i in range(len(asteroids)):
            if len(stack)==0 or asteroids[i]>0 or stack[-1]<0:
                stack.append(asteroids[i])
            else:
                while len(stack)!=0 and abs(asteroids[i])>stack[-1] and stack[-1]>0:
                    stack.pop()
                    
                if len(stack)!=0 and abs(asteroids[i])==stack[-1] and stack[-1]>0:
                    stack.pop()
                    continue
                if len(stack)==0 or stack[-1]<0:
                    stack.append(asteroids[i])    
        return stack

        