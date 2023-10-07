// function checkIfPangram(sentence:string="asdfghjkl"):any {
    // let ans=sentence.map((i)=>{
        // ans2:String
        // let ans2=sentence.map((t)=>{
            //     if (i!=t) {
                //         return true
                //     } else {
                    //         return false
                    //     }
                    //     })
                    // })
                    // };
                    // console.log(checkIfPangram());
                    
// function checkIfPangram(sentence:string):any {
// for (let i = 0; i < sentence.length; i++) {
//     for (let j = sentence.length-1; j >=0 ; j--) {
//         if (i!=j) {
//             return true
//         } else if (i!=j) {
//             return true
//         }
//         else {
//             return false
//         }
        
//     }
// }
// }
// console.log(checkIfPangram("danish"));


function checkIfPangram(sentence: string): boolean {
    //   return new Set(sentence).size === 26
    let arr:string[]=[]
    arr.push(sentence.charAt(0))
    for (let index = 1; index < sentence.length; index++) {
        let ch:string=sentence.charAt(index)
        for (let j = 0; j < arr.length; j++) {
            const element = arr[j];
            if (ch==element) {
                return false
            } else {
                arr.push(ch);
            }
        }
    }
    return true
    }
console.log(checkIfPangram());



