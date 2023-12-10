// Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
// An input string is valid if:
// Open brackets must be closed by the same type of brackets.
// Open brackets must be closed in the correct order.
// Every close bracket has a corresponding open bracket of the same type.
 // Example 1:
// Input: s = "()"
// Output: true
// Example 2:
// Input: s = "()[]{}"
// Output: true
// Example 3:
// Input: s = "(]"
// Output: false
 
function isValid(s: string): boolean {
    var ft:boolean=true
    if(s.length%2==1){
        return false;
    }

    for (let i = 0; i < s.length; i++) {
if (s[i]=="("&&s[i+1]==")") {
    ft=true
}         
else if (s[i]==")"&&s[i-1]=="(") {
    ft=true
}
else if (s[i]=="{"&&s[i+1]=="}") {
    ft=true
}
else if (s[i]=="}"&&s[i-1]=="{") {
    ft=true
}
else if (s[i]=="["&&s[i+1]=="]") {
    ft=true
}
else if (s[i]=="]"&&s[i-1]=="[") {
    ft=true
} 
else if (s[i]=="["&&s[i+1]=="{"&&s[i+2]=="}"&&s[i+3]=="]") {
    ft=true
} 
else if (s[i]=="{"&&s[i+1]=="["&&s[i+2]=="]"&&s[i+3]=="}") {
    ft=true
} 
else if (s[i]=="("&&s[i+1]=="{"&&s[i+2]=="}"&&s[i+3]==")") {
    ft=true
} 
else if (s[i]=="{"&&s[i+1]=="("&&s[i+2]==")"&&s[i+3]=="}") {
    ft=true
} 
else if (s[i]=="["&&s[i+1]=="("&&s[i+2]==")"&&s[i+3]=="]") {
    ft=true
} 
else if (s[i]=="("&&s[i+1]=="["&&s[i+2]=="]"&&s[i+3]==")") {
    ft=true
} 
else if (s[i]=="("&&s[i+1]=="["&&s[i+2]=="{"&&s[i+3]=="}"&&s[i+4]=="]"&&s[i+5]==")") {
    ft=true
} 
else if (s[i]=="["&&s[i+1]=="("&&s[i+2]=="{"&&s[i+3]=="}"&&s[i+4]==")"&&s[i+5]=="]") {
    ft=true
} 
else if (s[i]=="("&&s[i+1]=="{"&&s[i+2]=="["&&s[i+3]=="]"&&s[i+4]=="}"&&s[i+5]==")") {
    ft=true
} 
else if (s[i]=="{"&&s[i+1]=="["&&s[i+2]=="("&&s[i+3]==")"&&s[i+4]=="]"&&s[i+5]=="}") {
    ft=true
} 

 else{
    ft=false
}       
    }
    return ft
};