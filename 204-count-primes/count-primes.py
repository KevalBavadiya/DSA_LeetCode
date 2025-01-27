class Solution:
    def countPrimes(self, n: int) -> int:
        p = [1]*(n)
        j =2
        while j*j <= n :
            if p[j] == 1:
                for i in range(j*j, n, j):
                    p[i]=0
            j = j+1
        count = 0
        for i in range(2,n):
            if p[i] == 1:
                count += 1
        return count