function transpose(matrix) {
    var numRows = matrix.length;
    var numCols = matrix[0].length;
    // Initialize the transposed matrix with the correct dimensions
    var total = new Array(numCols);
    for (var j = 0; j < numCols; j++) {
        total[j] = new Array(numRows);
    }
    console.log(total);
}
console.log(transpose([[3, 5, 3], [6, 4, 7], [9, 4, 6]]));
