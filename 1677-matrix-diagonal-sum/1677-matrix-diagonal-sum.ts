function diagonalSum(mat: number[][]): number {
    let sum: number = 0
    for (let i = 0; i < mat.length; i++) {
        sum += mat[i][i]
    }
    let skipindex: number = -1
    if (mat.length % 2 == 1) {
        skipindex = Math.floor(mat.length / 2)
    }
    for (let j = mat.length - 1; j >= 0; j--) {
        if (j != skipindex) {
            sum += mat[(mat.length - 1) - j][j]

        }
    }
    return sum
};


