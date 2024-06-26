class Solution {
    public boolean isPalindrome(int x) {
        int dig,rev=0,n=x;
        if (x<0)
        return false;

        while(n!=0){
            dig=n%10;
            rev=rev*10+dig;
            n=n/10;
        }
        if(rev==x)
        return true;
        else
        return false;
    }
}