// Given a binary string s ​​​​​without leading zeros, return true​​​ if s contains at most one contiguous segment of ones. Otherwise, return false.
// Example 1:
// Input: s = "1001"
// Output: false
// Explanation: The ones do not form a contiguous segment.
// Example 2:
// Input: s = "110"
// Output: true
function checkOnesSegment(s: string): boolean { 
 
    for (let i = 0; i < s.length; i++) {
if (s[i]=="0"&&s[i+1]=="1") {
    return false
}  
}
return true      
};
console.log(checkOnesSegment("1"));



