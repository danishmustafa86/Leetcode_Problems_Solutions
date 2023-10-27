function matrixReshape(mat: number[][], r: number, c: number): number[][] {
    if ( mat.length* mat[0].length!=r*c) {
        return mat
    }
let array:number[][]=new Array(r).fill([]).map(()=>new Array(c))
let row:number=0
let col:number=0
for (let i = 0; i < mat.length; i++) {
    for (let j = 0; j < mat[i].length; j++) {
array[row][col]=mat[i][j]
col++
if (col==c) {
    col=0
    row++
}}};
return array
}
console.log(matrixReshape([[1,2],[3,4],[4,9]],2,3))
