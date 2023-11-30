function longestCommonPrefix(strs: string[]): string {
  let str:string=""
  for (let j = 0; j < strs[0].length; j++) {
    for (let i = 0; i < strs.length; i++) {
        if (strs[0][j]!=strs[i][j]) {
            return str
        }
    }    
    str+=strs[0][j]
  }
  return str
};