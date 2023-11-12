// Your friend is typing his name into a keyboard. Sometimes, when typing a character c, the key might get long pressed, and the character will be typed 1 or more times.
// You examine the typed characters of the keyboard. Return True if it is possible that it was your friends name, with some characters (possibly none) being long pressed.
// Example 1:
// Input: name = "alex", typed = "aaleex"
// Output: true
// Explanation: 'a' and 'e' in 'alex' were long pressed.

// function isLongPressedName(name: string, typed: string) {
//     if (name==typed) {
//         return true
//     }
//     for (let i = 0; i < typed.length; i++) {
// if (name[i]==typed[i]||typed[i+1]||typed[i+2]||typed[i+3]||typed[i+4]||typed[i+5]) {
//    return true 
// }        
//     }
//     return false
// };
// console.log(isLongPressedName("alex","aleex"));
function isLongPressedName(name: string, typed: string): boolean {
    if (name === typed) {
        return true;
    }

    let nameIndex = 0;
    for (let i = 0; i < typed.length; i++) {
        if (name[nameIndex] === typed[i]) {
            nameIndex++;
        } else if (i === 0 || typed[i] !== typed[i - 1]) {
            return false;
        }
    }

    return nameIndex === name.length;
}

// Example usage:
console.log(isLongPressedName("alex", "aaleex")); // Output: true

















