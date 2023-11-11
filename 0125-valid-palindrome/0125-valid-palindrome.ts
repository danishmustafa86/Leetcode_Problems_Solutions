function isPalindrome(s: string): boolean {
    let str: string = ""
    for (let i = 0; i < s.length; i++) {
        if (s[i] != "," && s[i] != ":" && s[i] != "'" && s[i] != "/" && s[i] != "?" && s[i] != "." && s[i] != "|" && s[i] != " "&& s[i] !="!"&& s[i] !="@"&& s[i] !="#"&& s[i] !="$"&& s[i] !="*"&& s[i] !="&"&& s[i] !="_" && s[i] !="%"&& s[i] !="["&& s[i] !="]"&& s[i] !="{"&& s[i] !="}"&& s[i] !="("&& s[i] !=")"&& s[i] !='"'&& s[i] !='__'&& s[i] !="-"&& s[i] !='+'&& s[i] !='<'&& s[i] !='>'&& s[i] !=';'&& s[i] !='^'&& s[i] !="`"&& s[i] !="~") {
            str += s[i]
        }
    }
    console.log(str);
    str = str.toLocaleLowerCase()
    let reversedStr: string = str.split("").reverse().join("");
    console.log(reversedStr);
    if (reversedStr === str) {
        return true;
    } else {
        return false;
    };
}