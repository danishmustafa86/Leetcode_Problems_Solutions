"use strict";
// A sentence is a list of words that are separated by a single space with no leading or
//  trailing spaces. Each word consists of lowercase and uppercase English letters.
// A sentence can be shuffled by appending the 1-indexed word position to each word then
//  rearranging the words in the sentence.
//example, "This is a sentence" shufled as "sentence4 a3 is2 This1" or "is2 sentence4 This1 a3".
// Given a shuffled sentence s containing no more than 9 words, reconstruct and return the
//  original sentence.
function sortSentence(s) {
    let arr = [];
    let n1 = "167";
    let n2 = parseInt(n1);
    console.log(n2);
    let strArr = s.split(' ');
    for (let i of strArr) {
        let index = parseInt(i.charAt(i.length - 1)) - 1;
        console.log(index);
        arr[index] = i.slice(0, i.length - 1);
    }
    ;
    return arr.join(' ');
}
;
console.log(sortSentence("how2 are3 you1"));
