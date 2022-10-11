class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: list[list[int]]) -> int:
        if(target<=startFuel):
            return 0
        elif len(stations)<1 or startFuel<stations[0][0]:
            return -1
            
        def helper(fuel,index):
            temp=index
            index+=1
            optimum=index
            while(len(stations)>index and stations[index][0]<fuel):
                if(stations[index][1]>stations[optimum][1]):
                    optimum = index
                index+=1
            if(temp==index-1):
                return temp
            else:
                return optimum
        
        i=-1
        count=0
        fuel=startFuel 
        while(i<len(stations)-1 and target>0):
            i= helper(fuel,i)
            target-= stations[i][0]
            fuel = fuel-stations[i][0] + stations[i][1]
            if(fuel<0):
                break
            count+=1
            if(fuel>=target):
                return count
        return -1
        
s = Solution()
s.minRefuelStops(1000,83,[[47,220],[65,1],[98,113],[126,196],[186,218],[320,205],[686,317],[707,325],[754,104],[781,105]])
                
            