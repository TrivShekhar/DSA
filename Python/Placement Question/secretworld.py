def secretword(n,s):
    a = "abcdefghijklmnopqrstuvwxyz"
    z = a[::-1]
    ans = ""
    for i in s:
        ans+=z[a.index(i)]
    return ans
print(secretword(5,"abaca"))