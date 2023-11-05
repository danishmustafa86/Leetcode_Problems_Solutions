// Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
// Example 1:
// Input: s = "Let's take LeetCode contest"
// Output: "s'teL ekat edoCteeL tsetnoc"
// Example 2:
// Input: s = "God Ding"
// Output: "doG gniD"



// // function reverseWords(s: string): string {
// function rverseWords(s: string): string {
//     const words = s.split(' ');
//     console.log(words);
//      // Split the sentence into words
//     const reversedWords = words.map(word => {
//         const reversedWord = word.split('').reverse().join(''); // Reverse the characters within each word
//         return reversedWord;
//     });

//     return reversedWords.join(' '); // Join the reversed words with whitespace to form the final sentence
// }
// console.log(rverseWords("Let's take LeetCode contest"));



// function reverWords(s: string): string {
//     let modifiedString: string = "";
//     const words = s.split('');

//     for (let i = 0; i < words.length; i++) {
//         modifiedString += words[i].split('').reverse().join(''); // Reverse the characters within each word
//         if (i < words.length - 1) {
//             modifiedString += ' '; // Add a space to separate words
//         }
//     }

//     return modifiedString;
// }

// console.log(reverWords("Let's take LeetCode contest"));




function reverseWords(s: string): string {
    let reversedSentence: string = ""
    const word = s.split(" ");
    for (let i = 0; i < word.length; i++) {
        const e = word[i];
        reversedSentence += e.split("").reverse().join("")
        if (i < word.length - 1) {
            reversedSentence += " "
        }

    }
    return reversedSentence
}
console.log(reverseWords("Let's take LeetCode contest"));
