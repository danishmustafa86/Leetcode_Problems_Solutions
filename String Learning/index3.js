"use strict";
// Input: command = "G()(al)"
// Output: "Goal"
// Explanation: The Goal Parser interprets the command as follows:
// G -> G
// () -> o
// (al) -> al
// The final concatenated result is "Goal".
function interpret(command) {
    let str = "";
    for (let i = 0; i < command.length; i++) {
        if (command[i] == "G") {
            str = str.concat("G");
        }
        else if (command[i] == "(" && command[i + 1] == ")") {
            str = str.concat("o");
        }
        else if (command[i] == "(" && command[i + 3] == ")") {
            str = str.concat("al");
        }
        else {
            str = str.concat("");
        }
    }
    return str;
}
;
console.log(interpret("G()()()()(al)"));
