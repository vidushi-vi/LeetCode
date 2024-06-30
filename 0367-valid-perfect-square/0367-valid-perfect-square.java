class Solution {
    public boolean isPerfectSquare(int num) {
        if(num<1)
            return false;
        int check;
        check=(int)Math.sqrt(num);
        if (check*check==num)
            return true;
        else
            return false;
        
    }
}