class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        
        pre, curr = 0,1
        for i in range(2,n+1):
            pre,curr = curr, pre + curr

        return curr

        