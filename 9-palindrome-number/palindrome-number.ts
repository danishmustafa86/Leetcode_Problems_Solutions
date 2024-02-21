function isPalindrome(x: number): boolean {
    let st=x.toString()
    let sortedSt = st.split('').reverse().join(''); 
    return st==sortedSt
};