import math
from os import stat
'''
Henry is extremely keen on history and every one of the ages of his family. He does a ton of exploration and understands that he has plummeted from the incomparable Amaya line. After a ton of looking through old records and the most recent records of the general public, he can discover all the parent-kid connections in his family right from the extraordinary ruler Ming of the tradition to himself.

These connections are given in the structure a direct exhibit where emperor is at the main position and his kids are at pos (2i + 1) and (2i + 2)

This is the pattern followed throughout.

Henry needs to sort out every one of the kin of individual X from the information.

Write a program for Henry to figure out all the siblings of person X from the data.
Return the sorted list of all of Henry’s siblings.

If no sibling return {-1}

input 1: N, the length of the array
input2: An array representing the ancestral tree
input 3 : X, the person whose siblings are sought.
output – return the array of all siblings in increasingly sorted order.
'''
arr = input().split()
x = input()
ind = arr.index(x)
if(ind==0):
    print(-1)
else:
    startind=0
    level=0
    while(startind<len(arr)):
        endind = startind + 2**level
        if(ind > startind and ind < endind):
            break
        startind = startind + 2**level
        level+=1
    print(arr[startind:endind])


        





