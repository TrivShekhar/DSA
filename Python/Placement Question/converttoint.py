def myAtoi( s: str) -> int:
        isneg=False
        nu=0
        for i in s:
            if i==" ":
                continue
            elif i=="-":
                isneg=True
            elif i=="+":
                isneg=False
            elif i<="9" and i>="0":
                nu=nu*10+int(i)
            
        if isneg:
            return -nu
        else:
            return nu
print(myAtoi("words and 987"))     