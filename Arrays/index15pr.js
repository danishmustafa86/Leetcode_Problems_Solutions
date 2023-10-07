function diagonalSum(mat) {
    var sum = 0;
    for (var i = 0; i < mat.length; i++) {
        console.log("mat[i][i] : ", mat[i][i]);
        sum += mat[i][i];
    }
    var skipindex = -1;
    if (mat.length % 2 == 1) {
        skipindex = Math.floor(mat.length / 2);
    }
    for (var j = mat.length - 1; j >= 0; j--) {
        if (j != skipindex) {
            sum += mat[(mat.length - 1) - j][j];
        }
    }
    return sum;
}
;
// console.log(diagonalSum([[8]]));
console.log(diagonalSum([[1, 3, 4], [4, 15, 3], [9, 8, 3]]));
// console.log(diagonalSum([[1, 3, 4, 7], [8, 4, 1, 6], [4, 15, 3, 2], [9, 8, 3, 6]]));
