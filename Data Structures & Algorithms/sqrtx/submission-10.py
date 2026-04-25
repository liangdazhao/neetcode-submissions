class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0

        res = 1
        l, r = 0, x

        while l <= r:
            m = (l+r)//2
            if m*m <= x:
                res=m
                l=m+1
            else:
                r=m-1
        return res
        
                

            