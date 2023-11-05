// Input: moves = "UD"
// Output: true
// function judgeCircle(moves: string): boolean {
//     for (let i = 0; i < moves.length; i++) {
//         if (moves[i] == "L" && moves[i + 1] == "R" && moves[i + 2] == "U" && moves[i + 1] == "D") {
//             return true
//         }
//         else if (moves[i] == "R" && moves[i + 1] == "L" && moves[i + 2] == "D" && moves[i + 1] == "U") {
//             return true
//         }
//         else if (moves[i] == "U" && moves[i + 1] == "D" && moves[i + 2] == "L" && moves[i + 1] == "R") {
//             return true
//         }
//         else if (moves[i] == "D" && moves[i + 1] == "U" && moves[i + 2] == "R" && moves[i + 1] == "L") {
//             return true
//         }
//         else if (moves[i] == "R" && moves[i + 1] == "L") {
//             return true
//         }
//         else if (moves[i] == "L" && moves[i + 1] == "R") {
//             return true
//         }
//         else if (moves[i] == "U" && moves[i + 1] == "D") {
//             return true
//         }
//         else if (moves[i] == "D" && moves[i + 1] == "U") {
//             return true
//         }
//         else {
//             return false
//         }
//     }
//     return false
// };
// console.log((judgeCircle("LRUD")));
function judgeCircle(moves) {
    var x = 0;
    var y = 0;
    for (var _i = 0, moves_1 = moves; _i < moves_1.length; _i++) {
        var move = moves_1[_i];
        if (move == "L")
            x++;
        if (move == "R")
            x--;
        if (move == "U")
            y++;
        if (move == "D")
            y--;
    }
    return x === 0 && y === 0;
}
