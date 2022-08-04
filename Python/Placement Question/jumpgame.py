class Solution:
    def jump(self, arr: List[int]) -> int:
        def helper(arr,index):
            mi=99999
            idx=index+1
            for i in range(index+1,index+arr[index]+1):
                if(i==len(arr)-1):
                    idx=i
                    break
                if(mi>(len(arr)-1)-(arr[i]+i)):
                    idx=i
                    mi=len(arr)-1 - arr[i]-i
                
            return idx
        if(len(arr)<=1):
            return 0
        jump=0
        i=0
        while(True):
            if(i>=len(arr)-1):
                break
            index=helper(arr,i)
            jump+=1
            i=index
            
            
        return jump
            
