def longestPalindrome(s: str) -> str:
    palindrome=""
    for i in range(len(s)):
        pal=s[i]
        if(len(pal)>len(palindrome)):
            palindrome=pal
        right=i+1
        while(right<len(s) and s[i]==s[right]):
            pal=s[i:right+1]
            if(len(pal)>len(palindrome)):
                palindrome=pal
            right+=1
        left=i-1
        while(left>=0 and right<len(s)):
            if(s[left:i]==s[right:i:-1]):
                pal=s[left:right+1]
                if(len(pal)>len(palindrome)):
                    palindrome=pal                    
                left-=1
                right+=1
            else:
                break
    return palindrome
longestPalindrome("tattarrattat")