class Solution {
    public int[] searchRange(int[] nums, int target) {
        int n=nums.length;
        int[] result = new int[2];
        result[0] = firstocc(nums, n, target);
        result[1] = lastocc(nums, n, target);
        return result;
    }
        int firstocc(int[] nums,int n,int target){
            int s=0,e=n-1,ans=-1,mid=s+(e-s)/2;
            while(s<=e){
                if(nums[mid]==target){
                    ans=mid;
                    e=mid-1;
                }
                else if(target>nums[mid])
                       s=mid+1;
                else
                    e=mid-1;
                mid=s+(e-s)/2;
            }
            return ans;
        }
      int lastocc(int[] nums,int n,int target){
            int s=0,e=n-1,ans=-1,mid=s+(e-s)/2;
            while(s<=e){
                if(nums[mid]==target){
                    ans=mid;
                    s=mid+1;
                }
                else if(target>nums[mid])
                       s=mid+1;
                else
                    e=mid-1;
                mid=s+(e-s)/2;
            }
            return ans;
        } 
        
            
        
        
    }
