function interpret(command: string): string {
    let str:string=""
for (let i = 0; i < command.length; i++) {
    if (command[i]=="G") {
        str=str.concat("G")
    }
    else if (command[i]=="(" && command[i+1]==")") {
        str=str.concat("o")
    }
    else if (command[i]=="(" && command[i+3]==")") {
        str=str.concat("al")
    }
    // else{
    //     str=str.concat("")
    // }
}
return str
};