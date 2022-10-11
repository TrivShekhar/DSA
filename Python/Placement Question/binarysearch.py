class Solution:
    def search(self, nums:list[int], target: int) -> int:
        def helper(l,r):
            mid=(l+r)//2
            if(l>=r):
                return -1
            elif(nums[mid]==target):
                return mid
            elif(nums[mid]<target):
                return helper(mid,r)
            else:
                return helper(l,mid)
        return helper(0,len(nums)-1)
sol=Solution()
print(sol.search([-1,0,3,5,9,12],2))