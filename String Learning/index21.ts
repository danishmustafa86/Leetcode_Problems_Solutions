// You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.
// Return the merged string.
// Example 1:
// Input: word1 = "abc", word2 = "pqr"
// Output: "apbqcr"

function merging(w1:string,w2:string):string{
    let merg="";
    for(let i:number=0;i<Math.max(w1.length,w2.length);i++){
        if(i<w1.length) merg+=w1[i]
        if(i<w2.length) merg+=w2[i]
    }
    return merg
}