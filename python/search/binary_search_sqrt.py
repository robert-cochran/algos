class Solution:
    def mySqrt(self, x: int) -> int:
   
        if x==0:
            return 0
       
        lo, hi = 1, x
        half = x
        while half:
            hi = half
            half = half//2
            if half*half<x:
                lo = half
                half = 0

    
        for elem in range(hi, 0, -1):
            if ((elem*elem) <= x):
                return elem
            
        return 1
        
