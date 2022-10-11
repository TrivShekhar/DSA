k=int(input())
table=[0 for i in range(k+1)]    
table[0]=1
for i in range(3, k+1):
    table[i] += table[i-3]
for i in range(5, k+1):
    table[i] += table[i-5]
for i in range(10, k+1):
    table[i] += table[i-10]
print(table[k])