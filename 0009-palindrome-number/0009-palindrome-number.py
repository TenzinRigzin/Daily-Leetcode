class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=list(str(x))
        self=x[::-1]
        if self[0]=='-':
            return False
        
        

        print(x,self)
        if (self==x):
            return True
        else:
            return False