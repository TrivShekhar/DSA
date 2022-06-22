def uniqueemails(emails):
    emailset=set()
    for email in emails:
        local,domain=email.split("@")
        local=local.split('+')[0]
        first=local.replace('.','')
        print(first+domain)
        emailset.add(first+domain)
    return len(emailset)
li= input().split()
print(uniqueemails(li))

        
