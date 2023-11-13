function longestCommonPrefix(strs: string[]): string {
    let str: string = "";
    
    if (strs.length === 0) {
        return str;
    }

    for (let j = 0; j < strs[0].length; j++) {
        for (let i = 1; i < strs.length; i++) {
            if (j >= strs[i].length || strs[i][j] !== strs[0][j]) {
                return str;
            }
        }
        str += strs[0][j];
    }

    return str;
}

console.log(longestCommonPrefix(["flower", "flow", "flight"]));
