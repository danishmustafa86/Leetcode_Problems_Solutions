function matrixReshape(mat, r, c) {
    if (mat.length * mat[0].length != r * c) {
        return mat;
    }
    var array = new Array(r).fill([]).map(function () { return new Array(c); });
    var row = 0;
    var col = 0;
    for (var i = 0; i < mat.length; i++) {
        for (var j = 0; j < mat[i].length; j++) {
            array[row][col] = mat[i][j];
            col++;
            if (col == c) {
                col = 0;
                row++;
            }
        }
    }
    ;
    return array;
}
console.log(matrixReshape([[1, 2], [3, 4], [4, 9]], 2, 3));
