class Solution(object):
    def backtrack(self, open_count, close_count, n, current, result):
        if open_count == n and close_count == n:
            result.append(current)
            return
        if open_count < n:
            self.backtrack(open_count + 1, close_count, n, current + '(', result)
        if close_count < open_count:
            self.backtrack(open_count, close_count + 1, n, current + ')', result)
    
    def generateParenthesis(self, n):
        result = []
        self.backtrack(0, 0, n, '', result)
        return result