// Given a string s consisting of words and spaces, return the length of the last word in the string.
// A word is a maximal 
// substring
//  consisting of non-space characters only.
// Example 1:
// Input: s = "Hello World"
// Output: 5
// Explanation: The last word is "World" with length 5.
function lengthOfLastWord(s) {
    var words = s.split(' ');
    var n = words.length - 1;
    var n2 = 0;
    if (words[n] != " ") {
        n2 = words[n].length;
    }
    if (words[n] == " ") {
        n2 = words[n - 1].length;
    }
    return n2;
}
// let n2:number=words[n].length
// for (let j = 0; j < words.length; j++) {
//     if (words.) {
//     }
// }
// console.log(words,"words length");
// let n:number=0
// for (let i = words.length-1; i >=0; i++) {
//    n=words[i].length
//    console.log(words[i].length,"nnnnnnnnn");
//    return n
// }
// return n
console.log(lengthOfLastWord(" fly me   to   the mokjiioon"));
