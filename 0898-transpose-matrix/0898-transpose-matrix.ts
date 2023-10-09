function transpose(matrix: number[][]): number[][] {
    const numRows = matrix.length;
    const numCols = matrix[0].length;

    // Initialize the transposed matrix with the correct dimensions
    let total: number[][] = new Array(numCols);
    for (let j: number = 0; j < numCols; j++) {
        total[j] = new Array(numRows);
    }

    for (let i: number = 0; i < matrix.length; i++) {
        for (let j: number = 0; j < matrix[0].length; j++) {
            total[j][i] = matrix[i][j];
        }
    }
    return total;
};