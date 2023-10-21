function luckyNumbers (matrix: number[][]): number[] {
let lucknumber:number[]=[]

for (let i = 0; i < matrix.length; i++) {
    let index:number=0
let minindex:number=23990440
   for (let j = 0; j < matrix[i].length; j++) {
if(minindex>matrix[i][j]){
    minindex=matrix[i][j];
    index=j
   }
}
let bool:boolean=true
for (let j = 0; j < matrix.length; j++) {
if (matrix[i][index]<matrix[j][index]) {
    bool=false
    break;
}    
}
if (bool==true) {
    lucknumber.push(matrix[i][index])
}
};
return lucknumber
}
