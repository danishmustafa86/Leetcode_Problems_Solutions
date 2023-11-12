// Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
// Example 1:
// Input: haystack = "sadbutsad", needle = "sad"
// Output: 0
// Explanation: "sad" occurs at index 0 and 6.
// The first occurrence is at index 0, so we return 0.
// function strStr(haystack ="mississippi",needle ="issip"): number {
// function strStr(haystack ="mississippi",needle ="issip"): number {
//     let num1:number=-1
//     if (haystack.includes(needle)) {
//      for (let i = haystack.length-1; i >=0; i--) {
//         if (haystack[i]==needle[0]) {
//             num1=i
//         }
//      }
//     }
//   return num1

// };
// console.log(strStr());



function strStr(haystack = "mississippi", needle = "issip"): number {
    for (let i = 0; i <= haystack.length - needle.length; i++) {
        if (haystack.substring(i, i+needle.length) == needle) {
            return i
        }
    }
    return -1
}
console.log(strStr());