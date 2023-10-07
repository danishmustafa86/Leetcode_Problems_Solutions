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
function checkIfPangram(sentence) {
    for (var i = 0; i < sentence.length; i++) {
        for (var j = sentence.length - 1; j >= 0; j--) {
            if (i != j) {
                return true;
            }
            else if (i != j) {
                return true;
            }
            else {
                return false;
            }
        }
    }
}
console.log(checkIfPangram("danish"));
