class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def matchexpression(i, j):
            if(j==len(p)):
                return False
            if(p[j]=='.'):
                if(i==len(s)-1):
                    return True
                return matchexpression(i+1,j+1)
            elif(p[j]=='*'):
                if(s[i]==p[j-1]):
                    if(i==len(s)-1):
                        return True
                    return matchexpression(i+1,j)
                elif(p[j-1]=="."):
                    if(i==len(s)-1):
                        return True
                    return matchexpression(i+1,j)
                else:
                    return False
            elif(p[j]!=s[i]):
                return False
            elif(p[j]==s[i]):
                if(i==len(s)-1):
                    return True
                return matchexpression(i+1,j+1)
        ans=matchexpression(0,0)
        return ans
sol=Solution()
sol.isMatch("aa","a*")