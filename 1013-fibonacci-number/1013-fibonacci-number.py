class Solution:
    def fib(self, n: int) -> int:
        ''' optimal'''
        
        if n<=1:
            return n
        a,b=0,1
        for i in range(2,n+1):
            ans=a+b
            a,b=b,ans

        return b 
        
        '''# recursive code
        if n<=1:
            return n
        return self.fib(n-1)+self.fib(n-2) 

        # DP Tabulation approach

        if n<=1:
            return n
        dp=[0]*(n+1)
        dp[0]=0
        dp[1]=1
        for i in range(2,n+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[n]'''

        