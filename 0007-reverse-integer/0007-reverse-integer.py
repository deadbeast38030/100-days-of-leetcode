class Solution(object):
    def reverse(self, x):
        sign=-1 if x<0 else 1
        rever=sign*int(str(abs(x))[::-1]) 
        if rever>2**31-1 or rever<-2**31:
            return 0
        return rever 
        