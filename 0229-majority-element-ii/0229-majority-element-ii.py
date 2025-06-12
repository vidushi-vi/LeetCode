class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        count1,count2=0,0
        ele1,ele2=None,None
        for i in range(n):
            if count1==0 and ele2!=nums[i]:
                ele1=nums[i]
                count1=1
            elif count2==0 and ele1!=nums[i]:
                ele2=nums[i]
                count2=1
            elif ele1==nums[i]:
                count1+=1
            elif ele2==nums[i]:
                count2+=1
            else:
                count1-=1
                count2-=1
            
        count1,count2=0,0
        for i in range(n):
            if nums[i]==ele1:
                count1+=1
            elif nums[i]==ele2:
                count2+=1

        result=[]    
        if count1>(n//3):
            result.append(ele1)
        if count2>(n//3):
            result.append(ele2)

        return result


        