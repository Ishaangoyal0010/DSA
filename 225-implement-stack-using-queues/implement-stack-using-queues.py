class MyStack(object):

    def __init__(self):
        self.queue=[]

    def push(self, x):
        self.queue.append(x)
        for i in range(len(self.queue)-1):
            self.queue.append(self.queue.pop(0))
        

    def pop(self):
        if len(self.queue)==0:
            return 0
        else:
            return self.queue.pop(0)
        

    def top(self):
        return self.queue[0]

    def empty(self):
        if len(self.queue)==0:
            return True
        else:
            return  False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()