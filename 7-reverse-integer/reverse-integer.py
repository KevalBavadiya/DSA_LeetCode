class Solution:
    def reverse(self, n: int) -> int:
        temp = 0
        res = 0
        is_neg = False
        if n < 0: 
            is_neg = True
            n = abs(n)
        while n!=0:
            temp = n%10
            res = res*10 + temp
            n //=10
        if is_neg == True: res *=-1
        if pow(-2,31) <= res <= pow(2,31)-1:
            return res
        else:
            return 0


        