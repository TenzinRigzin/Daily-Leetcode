class Solution:
    def minChanges(self, s: str) -> int:
        str_list = list(s)
        count = 0
        for i in range(0,len(str_list)-1,2):
            if(str_list[i]!=str_list[i+1]):
                str_list[i]=str_list[i+1]
                count+=1
        return count