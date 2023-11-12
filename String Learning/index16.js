// A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
// Given a string s, return true if it is a palindrome, or false otherwise.
// Example 1:
// Input: s = "A man, a plan, a canal: Panama"
// Output: true
// Explanation: "amanaplanacanalpanama" is a palindrome.
// let s:string="A man, a plan, a canal: Panama"
// let f:string[]=s.
// console.log(f);
// function isPalindrome(s: string): boolean {
//     let str: string = ""
//     for (let i = 0; i < s.length; i++) {
//         if (s[i] != "," && s[i] != ":" && s[i] != "'" && s[i] != "/" && s[i] != "?" && s[i] != "." && s[i] != "|" 
//         && s[i] != " "&& s[i] !="!"&& s[i] !="@"&& s[i] !="#"&& s[i] !="$"&& s[i] !="*"
//         && s[i] !="&"&& s[i] !="_" && s[i] !="%"&& s[i] !="["&& s[i] !="]"&& s[i] !="{"
//         && s[i] !="}"&& s[i] !="("&& s[i] !=")"&& s[i] !='"'&& s[i] !=``) {
//             str += s[i]
//         }
//     }
//     console.log(str);
//     str = str.toLocaleLowerCase()
//     let reversedStr: string = str.split("").reverse().join("");
//     console.log(reversedStr);
//     if (reversedStr === str) {
//         return true;
//     } else {
//         return false;
//     };
// }
// console.log(isPalindrome("A man, a plan, a canal: Panama"));
// console.log(isPalindrome("A man, a plan, a canal: Panama"));
// OTHER METHOD
function isPalindrome(s) {
    var str = "";
    for (var i = 0; i < s.length; i++) {
        if ((s[i] >= "a" && s[i] <= "Z") ||
            (s[i] >= "0" && s[i] <= "9")) {
            str += s[i];
        }
    }
    console.log(str);
    str = str.toLocaleLowerCase();
    console.log(str);
    var reversedStr = str.split("").reverse().join("");
    console.log(reversedStr);
    if (reversedStr === str) {
        return true;
    }
    else {
        return false;
    }
    ;
    console.log("ojoihln");
}
console.log(isPalindrome("race a car"));
console.log("jkhuchvjh");
