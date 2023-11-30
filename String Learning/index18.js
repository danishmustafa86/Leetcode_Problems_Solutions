// Write a function to find the longest common prefix string amongst an array of strings.
// If there is no common prefix, return an empty string "".
// Example 1:
// Input: strs = ["flower","flow","flight"]
// Output: "fl"
// Example 2:
// Input: strs = ["dog","racecar","car"]
// Output: ""
// Explanation: There is no common prefix among the input strings.
function longestCommonPrefix(strs) {
    var str = "";
    var st = "";
    for (var i = 0; i < strs.length; i++) {
        for (var j = 0; j < strs[i].length; j++) {
            if (strs[i][j] === strs[i + 1][j]) {
                str += strs[i][j];
            }
        }
    }
    return str;
}
;
console.log(longestCommonPrefix(["flower", "flow", "flight"]));
