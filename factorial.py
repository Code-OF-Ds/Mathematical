# factorial
class Solution:
    def fact(self,n):
        res =1
        if n ==0:
            res= res*1
        else:
            res = n*self.fact(n-1)
        return res

obj = Solution()
print(obj.fact(4))
