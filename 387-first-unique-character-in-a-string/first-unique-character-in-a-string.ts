// function firstUniqChar(s: string): number {
//     let n:number=-1
//     let ns:string[]=s.split('')
//     for(let i=0;i<s.length;i++){
//         for(let j=1;j<s.length;j++){
//             if(s[i]===s[j]){
//                 ns.splice(i,1)
//                 ns.splice(j,1)
//             }        }    }
//     if(ns.length>0){
//     var m=ns[0]
//     }
//     for(let k=0;k<s.length;k++){
//         if(s[k]===m){
//             n=k
//         }
//     }
    
//     return n
// };


// function firstUniqChar(s: string): number {
//     let ns: string[] = s.split('');
    //     // Iterate through the string to find the first non-repeating character
//     for (let i = 0; i < ns.length; i++) {
//         let isUnique = true;
//         for (let j = 0; j < ns.length; j++) {
//             if (i !== j && ns[i] === ns[j]) {
//                 // If a duplicate character is found, mark it as not unique
//                 isUnique = false;
//                 break;
//             }//         }
//         // If the current character is unique, return its index
//         if (isUnique) {
//             return i;//         }
//     }
    //     // If no unique character is found, return -1
//     return -1;
// }
function firstUniqChar(s: string): number {
    let ns: string[] = s.split('');
    for(let i=0;i<ns.length;i++){
        let unique=true
        for(let j=0;j<ns.length;j++){
            if(i!==j && ns[i]===ns[j]){
                unique=false
                break;
            }        }
        if(unique){
            return i
        }
    }
    return -1
}
