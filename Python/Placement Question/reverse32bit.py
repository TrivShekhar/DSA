def reverse(x: int) -> int:
    prange=2147483647//10
    nrange=-2147483648//10
    nu=0
    x=abs(x)
    while(x!=0):
        if(nu<nrange or nu>prange):
            return 0
        nu=nu*10+x%10
        x=x//10
    return nu
print(reverse(-1))