
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        j=0
        ans=-1
        if(len(haystack)<len(needle)):
            return ans
        for i,val in enumerate(haystack):
            if(j==len(needle)):
                return ans
            elif(needle[j]==val and j==0):
                j+=1
                ans=i
            elif(needle[j]==val and j!=0):
                j+=1
            else:
                j=0
                ans=-1
                if(needle[j]==val and j==0):
                    j+=1
                    ans=i
                
        return ans            
        
sol = Solution()
sol.strStr("mississippi","issip")