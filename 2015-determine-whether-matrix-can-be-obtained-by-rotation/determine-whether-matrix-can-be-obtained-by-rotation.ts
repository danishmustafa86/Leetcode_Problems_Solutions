function rotate(matrix: number[][]): void {
    let x = 0;
    let y = matrix.length - 1;

    while (x < y) {
        for (let i = 0; i < y - x; i++) {
          const topLeft = matrix[x][x + i];
          matrix[x][x + i] = matrix[y - i][x];
          matrix[y - i][x] = matrix[y][y - i];
          matrix[y][y - i] = matrix[x + i][y];
          matrix[x + i][y] = topLeft;
        }
        y--;
        x++;
    }
};

function findRotation(mat: number[][], target: number[][]): boolean {
    for (let i = 0; i < 4; i++) {
      if (mat.every((row, rowIdx) => row.every((el, colIdx) => el === target[rowIdx][colIdx]))) {
        return true;
      } 
      rotate(mat);
    }
  return false;
};