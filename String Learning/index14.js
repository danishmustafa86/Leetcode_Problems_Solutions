// Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
// Example 1:
// Input: haystack = "sadbutsad", needle = "sad"
// Output: 0
// Explanation: "sad" occurs at index 0 and 6.
// The first occurrence is at index 0, so we return 0.
function strStr(haystack, needle) {
    if (haystack === void 0) { haystack = "busadtsad"; }
    if (needle === void 0) { needle = "sad"; }
    var num1 = -1;
    // if (haystack.includes(needle)) {
    for (var i = haystack.length - 1; i >= 0; i--) {
        if (haystack[i] == needle[0]) {
            num1 = i;
        }
    }
    // }
    return num1;
}
;
console.log(strStr());
