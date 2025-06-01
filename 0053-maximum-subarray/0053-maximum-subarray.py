class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max=-sys.maxsize
        sum=0
        n=len(nums)
        for i in range(n):
            sum+=nums[i]
            if sum>max:
                max=sum
            if sum<0:
                sum=0
    
        return max