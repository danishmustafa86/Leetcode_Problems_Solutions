"use strict";
// Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.
// A string is represented by an array if the array elements concatenated in order forms the string.
// Example 1:
// Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
// Output: true
// n2=n2.concat(word2[i])
// if (n1===n2) {
//     return true
// }
// function arrayStringsAreEqual(word1: string[], word2: string[]): boolean {
// let n1:string=''
// let n2:string=''
// for (let i = 0; i < word1.length; i++) {
//     n1=n1.concat(word1[i])
// }
// for (let j = 0; j < word2.length; j++) {
//     n2=n2.concat(word2[j])
// }
// if (n1===n2) {
//         return true
//     }
// return false
// };
// console.log(arrayStringsAreEqual(["ab", "c"],["a", "bc"]));
function arrayStringsAreEqual(word1, word2) {
    let n1 = word1.join("");
    let n2 = word2.join("");
    if (n1 === n2) {
        return true;
    }
    return false;
}
;
console.log(arrayStringsAreEqual(["ab", "c"], ["a", "bc"]));
