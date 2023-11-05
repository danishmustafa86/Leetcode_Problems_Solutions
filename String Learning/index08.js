// You are given a string s of even length. Split this string into two halves of equal lengths, and let a be the first half and b be the second half.
// Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains uppercase and lowercase letters.
function halvesAreAlike(s) {
    var vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"];
    var halve1 = s.slice(0, s.length / 2);
    var halve2 = s.slice(s.length / 2, s.length);
    var leftside = 0;
    var rightside = 0;
    for (var i = 0; i < halve1.length; i++) {
        if (vowels.includes(halve1[i])) {
            leftside++;
        }
        if (vowels.includes(halve2[i])) {
            rightside++;
        }
    }
    return leftside == rightside;
}
;
console.log(halvesAreAlike("good"));
