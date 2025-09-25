function luckyNumbers(matrix: number[][]): number[] {
    let lucknumber: number[] = []

    for (let i = 0; i < matrix.length; i++) {
        let indx: number = 0
        let minindex: number = 23990440
        for (let j = 0; j < matrix[i].length; j++) {
            if (minindex > matrix[i][j]) {
                minindex = matrix[i][j];
                indx = j
            }
        }
        let bool: boolean = true
        for (let j = 0; j < matrix.length; j++) {
            if (matrix[i][indx] < matrix[j][indx]) {
                bool = false
                break;
            }
        }
        if (bool == true) {
            lucknumber.push(matrix[i][indx])
        }
    };
    return lucknumber
}
