class Solution:
    def climbStairs(self, n: int) -> int:
        fib, nfib = 0, 1
        while n>0:
            n-=1
            nfib, fib = nfib+fib, nfib
        return nfib
        