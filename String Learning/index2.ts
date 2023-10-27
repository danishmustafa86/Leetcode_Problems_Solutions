// Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
// Output: "leetcode"
// function restoreString(s: string, indices: number[]): string {
//     let mstring:string=""
//     for (let j = 0; j < indices.length; j++) {
//             for (let i = 0; i < s.length; i++) {
//     if (indices[j]==i) {
//         mstring= mstring.concat(s[i])
//     }
// }    
// }
//  return mstring
// };

// function restoreString(s: string, indices: number[]): string {
//     let mstring: string = "";

//     for (let j = 0; j < indices.length; j++) {
//         mstring =mstring.concat(s[j])
//         // mstring = mstring.concat(s[indices[j]]);
//     }

//     return mstring;
// }

// console.log(restoreString("codeleet", [4, 5, 6, 7, 0, 2, 1, 3]));


function restoreString(s: string, indices: number[]): string {
    const shuffled: string[] = [];

    for (let i = 0; i < s.length; i++) {
        shuffled[indices[i]] = s[i];
    }

    return shuffled.join("")
}

console.log(restoreString("codeleet", [4, 5, 6, 7, 0, 2, 1, 3])); // Output: "leetcode"
console.log(restoreString("abc", [0, 1, 2])); // Output: "abc"


const fruits = ["apple", "banana", "cherry"];
const joinedString = fruits.join(); // Join elements with a comma and a space
console.log(joinedString);





































