function arrayStringsAreEqual(word1: string[], word2: string[]): boolean {
let n1:string=''
let n2:string=''
for (let i = 0; i < word1.length; i++) {
    n1=n1.concat(word1[i])
}
for (let j = 0; j < word2.length; j++) {
    n2=n2.concat(word2[j])
}
if (n1===n2) {
        return true
    }
return false
};