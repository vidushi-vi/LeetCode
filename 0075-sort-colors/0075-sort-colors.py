class Solution:
    def sortColors(self, nums: List[int]) -> None:

        n=len(nums)
        low=0
        mid=0
        high=n-1
        while mid<=high:
            if nums[mid]==0:
                nums[low],nums[mid]=nums[mid],nums[low]
                mid+=1
                low+=1
            elif nums[mid]==1:
                mid+=1
            else:
                nums[mid],nums[high]=nums[high],nums[mid]
                high-=1

        """
        Do not return anything, modify nums in-place instead.
        """
        