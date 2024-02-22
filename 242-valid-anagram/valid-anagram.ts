function isAnagram(s: string, t: string): boolean {
    if( s.length!==t.length)   return false
    s.split('')
    for(let i=0;i<s.length;i++){
        t=t.replace(s[i],"")
    }
    return !t.length
};


   // t.split('').forEach(char => s = s.replace(char, ""));