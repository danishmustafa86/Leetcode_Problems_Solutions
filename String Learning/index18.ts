// Write a function to find the longest common prefix string amongst an array of strings.
// If there is no common prefix, return an empty string "".
// Example 1:
// Input: strs = ["flower","flow","flight"]
// Output: "fl"
// Example 2:
// Input: strs = ["dog","racecar","car"]
// Output: ""
// Explanation: There is no common prefix among the input strings.

function longestCommonPrefix(strs: string[]): string {
  let str:string=""
  for (let j = 0; j < strs[0].length; j++) {
    for (let i = 0; i < strs.length; i++) {
        if (strs[0][j]!=strs[i][j]) {
            return str
        }
    }    
    str+=strs[0][j]
  }
  return str
};
console.log(longestCommonPrefix(["flower","flow","flight"]));







