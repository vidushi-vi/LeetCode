class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        left=0
        right=n-1
        
        for i in range(n):
            mid=(left+right)//2
            if target==nums[mid]:
                return mid
            elif target>nums[mid]:
                left=mid+1
            else:
                right=mid-1

        return -1
        