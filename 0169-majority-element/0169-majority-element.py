class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        count=0
        ele= None
        for i in range(n):
            if count==0:
                ele=nums[i]
                count=1
            elif ele==nums[i]:
                count+=1
            else:
                count-=1

        count1=0
        for i in range(n):
            if ele==nums[i]:
                count1+=1
        
        if count1>(n/2):
            return ele
        