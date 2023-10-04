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







