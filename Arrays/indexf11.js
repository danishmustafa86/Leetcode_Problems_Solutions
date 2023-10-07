function flipAndInvertImage(image) {
    var realArray = [];
    image.map(function (elm) {
        var reversing = elm.reverse();
        for (var i = 0; i < reversing.length; i++) {
            var elm_1 = reversing[i];
            if (elm_1 === 0) {
                reversing.splice(i, 1, 1);
            }
            else {
                reversing.splice(i, 1, 0);
            }
        }
        var reversed = realArray.push(reversing);
    });
    return realArray;
}
;
console.log(flipAndInvertImage([[1, 1, 0], [1, 0, 1], [0, 0, 0]]));
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
