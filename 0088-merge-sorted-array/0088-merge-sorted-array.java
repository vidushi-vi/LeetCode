class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int i=0,j=0, k=0;
        int[] nums3 = new int[m+n];
        while(i<m&&j<n)
        {
            if(nums1[i]<nums2[j])
            {
                nums3[k]=nums1[i];
                k++;
                i++;
            }
            else
            {
                nums3[k]=nums2[j];
                k++;
                j++;
            }
            
        }
        while(i<m)
        {
            nums3[k]=nums1[i];
            i++;
            k++;
        }
        while(j<n)
        {
            nums3[k]=nums2[j];
            j++;
            k++;
        }
        for(i=0;i<m+n;i++){
                nums1[i]=nums3[i];
            
        }
        
        
    }
}