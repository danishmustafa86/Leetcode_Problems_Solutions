function transpose(matrix: number[][]): number[][] {
    let total: number[][] = []
    for (let i:number = 0; i < matrix.length; i++) {
        for (let j:number = 0; j < matrix[0].length; j++) {
            // const element = array[j];
            total[j][i] = matrix[i][j];
        }
    }
    return total;
};

console.log(transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]));
