function isPalindrome(s: string): boolean {
    let str: string = ""
    for (let i = 0; i < s.length; i++) {
        if (s[i] != "," && s[i] != ":" && s[i] != "'" && s[i] != "/" && s[i] != "?" && s[i] != "." && s[i] != "|" && s[i] != " "&& s[i] !="!"&& s[i] !="@"&& s[i] !="#"&& s[i] !="$"&& s[i] !="*"&& s[i] !="&"&& s[i] !="_" && s[i] !="%"&& s[i] !="["&& s[i] !="]"&& s[i] !="{"&& s[i] !="}"&& s[i] !="("&& s[i] !=")"&& s[i] !='"'&& s[i] !='__'&& s[i] !="-"&& s[i] !='+'&& s[i] !='<'&& s[i] !='>'&& s[i] !=';'&& s[i] !='^'&& s[i] !="`"&& s[i] !="~") {
            str += s[i]
        }
    }
    str = str.toLocaleLowerCase()
    let reversedStr: string = str.split("").reverse().join("");
    if (reversedStr === str) {
        return true;
    } else {
        return false;
    };
}