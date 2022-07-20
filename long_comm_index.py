class Solution:
    def find_index(self,strl):
        comm = strl[0]    
        ans = strl[0]
        for i in range(1,len(strl)):
            s = strl[i]
            temp = ""
            for j in range(min(len(comm),len(s))):
                if(comm[j]!=s[j]):
                    break
                else:
                    temp += s[j]
            if(len(temp)<len(ans)):
                ans = temp

        return ans

strl = eval(input())
obj1 = Solution()
print(obj1.find_index(strl))
