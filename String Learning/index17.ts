// Given a string s, return true if the s can be palindrome after deleting at most one character from it.
// Example 1:
// Input: s = "aba"
// Output: true
// Example 2:
// Input: s = "abca"
// Output: true
// Explanation: You could delete the character 'c'.

function validPalindrome(s: string) {
let  right:number= s.length-1;
for (let i = 0; i < s.length; i++) {
if (s.length%2==0) {
    if (i<(right-2)&&s[i]==s[right]) {
        return true
    } else {
        return false
        
    }
} 
if (s.length%2==1) {
    if (i<(right-1)&&s[i]==s[right]) {
        return true
    } else {
        return false
        
    }
}   
}
};



