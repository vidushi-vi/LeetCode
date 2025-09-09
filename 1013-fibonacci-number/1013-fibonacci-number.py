class Solution:
    def fib(self, n: int) -> int:
        ''' brute force
        
        if n<=1:
            return n
        a,b=0,1
        for i in range(2,n+1):
            a,b=b,a+b

        return b '''
        
        # recursive code
        if n<=1:
            return n
        return self.fib(n-1)+self.fib(n-2)

        