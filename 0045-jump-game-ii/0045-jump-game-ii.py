class Solution:
    def jump(self, nums: List[int]) -> int:
        l=r=0
        jumps=0
        n=len(nums)
        while(r<n-1):
            farthest=0
            for i in range(l,r+1):
                farthest=max(farthest,i+nums[i])
            l=r+1
            r=farthest
            jumps+=1
        return jumps       
                

        