// function minimumLength(s: string): number {
//     let ar=s.split("")
//     for (let i=0;i<ar.length;i++){
//         for (let j=ar.length-1;j>=0;j--){
//             if(ar[i]==ar[j] && i!=j ){
//                 ar.splice(i,1)
//                 ar.splice(j,1)
//             }
//         }
//     }
//     return ar.length
// };
function minimumLength(s: string): number {
    let left = 0;
    let right = s.length - 1;

    // Continue removing prefixes and suffixes while left pointer is less than right pointer
    while (left < right) {
        // If characters at left and right pointers are equal, find the next different character from both sides
        if (s[left] === s[right]) {
            const currentChar = s[left];
            // Move left pointer to the right until a different character is encountered or left pointer exceeds right pointer
            while (left < right && s[left] === currentChar) {
                left++;
            }
            // Move right pointer to the left until a different character is encountered or right pointer exceeds left pointer
            while (left <= right && s[right] === currentChar) {
                right--;
            }
        } else {
            // If characters at left and right pointers are different, break the loop
            break;
        }
    }

    // Calculate and return the remaining length after removing prefix and suffix
    return Math.max(right - left + 1, 0);
}
