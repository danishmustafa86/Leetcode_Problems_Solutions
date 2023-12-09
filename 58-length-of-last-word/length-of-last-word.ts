function lengthOfLastWord(s: string): number {
let st:string=s.trim()
const wordsArray = st.split(/\s+/);
let numLength=wordsArray[wordsArray.length-1]
return numLength.length
}