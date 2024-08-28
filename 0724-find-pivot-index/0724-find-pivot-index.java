class Solution {
    public int pivotIndex(int[] nums) {
        int leftsum=0, rightsum=0, index;
        int totalsum=0;
        for(int i=0;i<nums.length;i++)
        {
            totalsum+=nums[i];
        }
        for(int i=0;i<nums.length;i++)
        {
            if(leftsum==totalsum-leftsum-nums[i])
                return i;
            leftsum+=nums[i];
        }
        return -1;
        
    }
}