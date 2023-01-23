def decrypt(s):
    ans=""
    for i in range(0,len(s),2):
        ans+=s[i]*int(s[i+1])
    return ans

print(decrypt(input()))
