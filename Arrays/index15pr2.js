function diaginalmat(matric) {
    var total = 0;
    for (var i = 0; i < matric.length; i++) {
        total += matric[i][i];
    }
    var skipnum = -1;
    if (matric.length % 2 == 1) {
        skipnum = Math.floor(matric.length / 2);
    }
    for (var i = 0; i < matric.length; i++) {
        if (i != skipnum) {
            total += matric[(matric.length - 1) - i][i];
        }
    }
    return total;
}
console.log(diaginalmat([[8]]));
console.log(diaginalmat([[1, 3, 5], [5, 3, 6], [9, 0, 7]]));
console.log(diaginalmat([[1, 3, 2, 5], [5, 3, 9, 6], [9, 0, 4, 7], [3, 5, 7, 4]]));
