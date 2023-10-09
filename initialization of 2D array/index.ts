function transpose(matrix: number[][]): number[][] {
    // const numRows = matrix.length;
    // const numCols = matrix[0].length;

    // // Initialize the transposed matrix with the correct dimensions
    // let total: number[][] = new Array(numCols);
    // for (let j: number = 0; j < numCols; j++) {
    //     total[j] = new Array(numRows);
    // }
    const numrows=matrix.length
    const numcols=matrix[0].length
    let total:number[][]=new Array(numcols)
for (let f:number = 0; f < numcols; f++) {
    total[f]=new Array(numrows)
}
    for (let i: number = 0; i < matrix.length; i++) {
        for (let j: number = 0; j < matrix[0].length; j++) {
            total[j][i] = matrix[i][j];
        }
    }
    return total;
};
console.log(transpose([[1, 2, 3],[4, 5, 6],[7, 8, 9]]));
