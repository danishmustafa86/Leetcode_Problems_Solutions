function flipAndInvertImage(image: number[][]): number[][] {
    let realArray:number[][]=[]
    image.map((elm)=>{
        let reversing=elm.reverse()
        for (let i = 0; i < reversing.length; i++) {
            let elm = reversing[i];
            if (elm===0) {
                reversing.splice(i,1,1)
            } else {
                reversing.splice(i,1,0)
                
            }
        }
        let reversed=realArray.push(reversing)

    })
    return realArray
};
console.log(flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]));














//  realArray.map((el)=>{
// let inverting=el
// inverting.map((e)=>{
//     if (e===1) {
//         e=0
//     } else {
//         e=1
//     }
// })
// })