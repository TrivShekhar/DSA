'''
Given a positive whole number n, find the smallest number which has the very same digits existing in the whole number n and is greater than n. In the event that no such certain number exists, return – 1.

Note that the returned number should fit in a 32-digit number, if there is a substantial answer however it doesn’t fit in a 32-bit number, return – 1.

Example 1:
Input: n = 12
Output: 21

Explanation:  Using the same digit as the number of permutations, the next greatest number for 12 is 21.

Example 2:
Input: n = 21
Output: -1

Explanation:  The returned integer does not fit in a 32-bit integer
'''

inp= input()
possible=False
for i in range(len(inp)-1,0,-1):
    if(inp[i]>inp[i-1]):
        sortarr=inp[:i]
        nextarr=inp[i:]
        possible=True
        break
        
if(not possible):
    print(-1)
else:
    mi=sortarr[-1]
    inde=i
    for i in range(len(nextarr)):
        if(mi==sortarr[-1] and nextarr[i]>mi):
                mi=nextarr[i]
                inde=i
        else:
            if(mi>nextarr[i] and i>sortarr[-1]):
                mi=nextarr[i]
                inde=i
    num=sortarr[:len(sortarr)-1] + nextarr[inde]+nextarr[:inde]+sortarr[-1]+nextarr[inde+1:]
    print(num)

    
