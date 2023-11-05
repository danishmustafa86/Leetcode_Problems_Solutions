// Given an array of strings patterns and a string word, return the number of strings in
//  patterns that exist as a substring in word.
// A substring is a contiguous sequence of characters within a string.
// Example 1:
// Input: patterns = ["a","abc","bc","d"], word = "abc"
// Output: 3
// function numOfStrings(patterns: string[], word: string): number {
//     let num1: number = 0
//     for (let i = 0; i < patterns.length; i++) {
//         if (word.includes(patterns[i])) {
//             num1 += 1
//         }
//     }
//     return num1
// };
// console.log(numOfStrings(["a", "abc", "bc", "d"], "abc"));

// Input: patterns = ["a","abc","bc","d"], word = "abc"
// Output: 3
// if (patterns[i].includes(word)) {
//     num1 += 1;
// }
// function numOfStrings(patterns: string[] = ["a", "abc", "bc", "d"], word: string = "abc"): number {
//         let num1: number = 0;
//         for (let j = 0; j < patterns.length; j++) {
//                 if (word.includes(patterns[j])) {
//             num1++
//         }

//     }
//     return num1;
// }
// console.log(numOfStrings());

function numOfStrings(patterns: string[] = ["a", "abc", "bc", "d"], word: string = "abc"): number {
    let num1: number = 0;
    for (let j = 0; j < patterns.length; j++) {
        if (word.includes(patterns[j])) {
            num1++
        }

    }
    return num1;
}
console.log(numOfStrings(["a", "abc", "bc", "d"], "abc"));
