class Solution {
    public String longestPalindrome(String s) {
        int start = 0, end = 0, maxLen = 0;
        for (int i = 0; i < s.length(); i++){
            for (int j = i+1; j < s.length(); j++){
                String cur = s.substring(i,j+1);
                if (isPalindrome(cur) && (j - i + 1) > maxLen){
                    maxLen = j - i + 1 ;
                    start = i;
                    end = j;
                }
            }
        }
        return s.substring(start, end + 1);
    }
    private boolean isPalindrome(String str){
        int left = 0, right = str.length() - 1;
        while (left < right){
            if (str.charAt(left) != str.charAt(right)){
            return false;
            }
            left ++;
            right--;
        }
        return true;
    }
}