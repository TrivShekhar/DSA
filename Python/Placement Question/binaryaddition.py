class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i=-1
        j=-1
        ans=""
        carry="0"
        while(i >= -len(a) and j >=-len(b)):
            if(a[i]=="1" and b[j]=="1"):
                if(carry=="1"):
                    ans=ans+"1"
                    carry="1"
                else:
                    ans=ans+"0"
                    carry="1"
            elif(a[i]=="0" and b[j]=="0"):
                if(carry=="1"):
                    ans=ans+"1"
                    carry="0"
                else:
                    ans=ans+"0"
                    carry="0"
            else:
                if(carry=="1"):
                    ans=ans+"0"
                    carry="1"
                else:
                    ans=ans+"1"
                    carry="0"
            i-=1
            j-=1
        while(i >= -len(a)):
            if(a[i]=="1"):
                if(carry=="1"):
                    ans+="0"
                    carry="1"
                else:
                    ans+="1"
            elif(a[i]=="0"):
                if(carry=="1"):
                    ans+="1"
                    carry="0"
                else:
                    ans+="0"
            i-=1
        while(j >=-len(b)):
            if(b[j]=="1"):
                if(carry=="1"):
                    ans+="0"
                    carry="1"
                else:
                    ans+="1"
            elif(b[j]=="0"):
                if(carry=="1"):
                    ans+="1"
                    carry="0"
                else:
                    ans+="0"
            j-=1
        if(carry=="1"):
            ans+="1"
        return ans[::-1]
s=Solution()
s.addBinary("1111","1111")