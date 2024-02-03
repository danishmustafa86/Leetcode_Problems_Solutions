// function removeDuplicates(s: string): string {
//     let us:string[]=s.split('');
//     let i=0;
//     while(i < us.length - 1) {
//         if (us[i] === us[i + 1]) {
//             us.splice(i, 2);
//             i = 0;
//         } else {
//             i++;
//         }
//     }
//     return us.join('');
// }

// // Example usage:
// console.log(removeDuplicates("abbaca")); // Output: "ca"
// console.log(removeDuplicates("azxxzy")); // Output: "ay"
function removeDuplicates(s: string): string {
    let us:string[]=s.split('')
    let i=0
    while(i<us.length-1){
        if(us[i] === us[i + 1]){
            us.splice(i,2)
            i=0
        }       else{
            i++
        }
    }
    return us.join('')
}
   
   
   
   
        // Convert string to array

    // let chars: string[] = s.split('');
    // // Loop through the array to remove duplicates
    // for (let i = 0; i < chars.length - 1; i++) {
    //     if (chars[i] === chars[i + 1]) {
    //         // Remove the duplicate character
    //         chars.splice(i, 1);
    //         // After removing the duplicate, adjust the index
    //         i--;
    //     }