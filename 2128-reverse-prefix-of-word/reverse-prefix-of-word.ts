// function reversePrefix(word: string, ch: string): string {
//     let num: number = 0
//     let st: string = ""
//     if (word.includes(ch)) {
//         for (let i = 0; i < word.length; i++) {
//             if (word[i] == ch) {
//                 num = i
//                 for (let j = 0; j <= i; j++) {
//                     st += word[j];
//                 }
//                 st = st.split("").reverse().join("")
//                 break
//             }
//             if (i > num) {
//                 st += word[i]
//             }
//         }
//     }
//    return st+word.slice(num+1) || word;
//    }
    // } else {
    //     return word
    // } 
    // return   } st    OR





// function reversePrefix(word: string, ch: string): string {
//     let num: number = 0;
//     let st: string = "";
    
//     if (word.includes(ch)) {
//         for (let i = 0; i < word.length; i++) {
//             if (word[i] == ch) {
//                 num = i;
//                 for (let j = 0; j <= i; j++) {
//                     st += word[j];
//                 }
//                 st = st.split("").reverse().join("");
//                 break;
//             }
//             if (i > num) {
//                 st += word[i];
//             }
//         }
//     }
//     // Do nothing if ch is not present, just return the original word
//     return st || word;
// }




function reversePrefix(word: string, ch: string): string {
    let num: number = 0;
    let st: string = "";

    if (word.includes(ch)) {
        for (let i = 0; i < word.length; i++) {
            if (word[i] == ch) {
                num = i;
                for (let j = 0; j <= i; j++) {
                    st += word[j];
                }
                st = st.split("").reverse().join("");
                break;
            }
        }
    }
   else {
        return word
    } 
    return st + word.slice(num + 1)
}

// Test
console.log(reversePrefix("xyxzxe", "z")); // Output: "zxyxxe"
