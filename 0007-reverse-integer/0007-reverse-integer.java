class Solution {
    public int reverse(int x) {
        int digit,reverse=0;
        
         while(x!=0){
         digit= x%10;
         if (reverse > Integer.MAX_VALUE / 10 || reverse < Integer.MIN_VALUE / 10 ) {
                return 0;
                }
            
         reverse=reverse*10+digit;
         x=x/10;
         }
         return reverse;

        
    }
}