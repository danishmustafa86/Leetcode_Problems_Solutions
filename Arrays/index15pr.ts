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
// console.log(diagonalSum([[8]]));
console.log(diagonalSum([[1, 3, 4], [4, 15, 3], [9, 8, 3]]));
// console.log(diagonalSum([[1, 3, 4, 7], [8, 4, 1, 6], [4, 15, 3, 2], [9, 8, 3, 6]]));

