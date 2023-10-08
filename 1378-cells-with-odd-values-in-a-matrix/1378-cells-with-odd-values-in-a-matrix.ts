function oddCells(m, n, indices){
    let grid = [...Array(m)].map(e => Array(n).fill(0))
    let count = 0

    for(let i = 0; i < indices.length;i++){
        let row = incrementRow(indices[i][0],grid)
        let col = incrementCol(indices[i][1],grid)
        grid = row[0]
        grid = col[0]
        count += row[1]
        count += col[1]
    }
    return count
};

function incrementRow(row,grid){
    let count = 0
    for(let i = 0; i < grid[row].length;i++){
        grid[row][i] = grid[row][i]+1
        if(grid[row][i] % 2 === 1){count++}
        else{count--}
    }
    return [grid,count]
}

function incrementCol(col,grid){
    let count = 0
    for(let i = 0; i < grid.length;i++){
        grid[i][col] = grid[i][col]+1
        if(grid[i][col] % 2 === 1){count++}
        else{count--}
    }
    return [grid,count]
}