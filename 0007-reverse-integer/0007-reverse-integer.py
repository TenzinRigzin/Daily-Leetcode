class Solution:
    def reverse(self, x: int) -> int:
        x_list=str(x)
        ans = str(abs(x))[::-1]
        
        ans=int(ans)
        if(x<0):
            ans=ans-2*ans
        range=2147483648
        if not -range<ans<range-1:
            return 0
        return ans

