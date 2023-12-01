function checkOnesSegment(s: string): boolean {
     if (s=="1") {
        return true
    }
    for (let i = 0; i < s.length; i++) {
        if (s[i]=="0"&&s[i+1]=="1") {
        return false
        }  
       
}
return true      
};
