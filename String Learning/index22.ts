// Given a 0-indexed string word and a character ch, reverse the segment of word that
//  starts at index 0 and ends at the index of the first occurrence of ch (inclusive). If the
//   character ch does not exist in word, do nothing.
// For example, if word = "abcdefd" and ch = "d", then you should reverse the segment that
//  starts at 0 and ends at 3 (inclusive). The resulting string will be "dcbaefd".
// Return the resulting string.
// Example 1:
// Input: word = "abcdefd", ch = "d"
// Output: "dcbaefd"

function reversePrefix(word: string, ch: string): string {
    let num: number = 0
    let st: string = ""
    if (word.includes(ch)) {
        for (let i = 0; i < word.length; i++) {
            if (word[i] == ch) {
                num = i
                for (let j = 0; j <= i; j++) {
                    st += word[j];
                }
                st = st.split("").reverse().join("")
                break
            }
            if (i > num) {
                st += word[i]
            }
        }
    }
    
    return st + word.slice(num + 1) || word;
}