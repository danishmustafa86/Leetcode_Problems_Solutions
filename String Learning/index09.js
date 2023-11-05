"use strict";
function freqAlphabets(s) {
    let stringoutput = "";
    for (let i = 0; i < s.length; i++) {
        if (s[i] == "1" && s[i + 2] != "#" && s[i + 1] != "#") {
            stringoutput += "a";
        }
        else if (s[i] == "2" && s[i + 2] != "#" && s[i + 1] != "#") {
            stringoutput += "b";
        }
        else if (s[i] == "3" && s[i + 2] != "#" && s[i + 1] != "#") {
            stringoutput += "c";
        }
        else if (s[i] == "4" && s[i + 2] != "#" && s[i + 1] != "#") {
            stringoutput += "d";
        }
        else if (s[i] == "5" && s[i + 2] != "#" && s[i + 1] != "#") {
            stringoutput += "e";
        }
        else if (s[i] == "6" && s[i + 2] != "#" && s[i + 1] != "#") {
            stringoutput += "f";
        }
        else if (s[i] == "7" && s[i + 2] != "#" && s[i + 1] != "#") {
            stringoutput += "g";
        }
        else if (s[i] == "8" && s[i + 2] != "#" && s[i + 1] != "#") {
            stringoutput += "h";
        }
        else if (s[i] == "9" && s[i + 2] != "#" && s[i + 1] != "#") {
            stringoutput += "i";
        }
        else if (s[i] == "1" && s[i + 1] == "0" && s[i + 2] == "#") {
            stringoutput += "j";
        }
        else if (s[i] == "1" && s[i + 1] == "1" && s[i + 2] == "#") {
            stringoutput += "k";
        }
        else if (s[i] == "1" && s[i + 1] == "2" && s[i + 2] == "#") {
            stringoutput += "l";
        }
        else if (s[i] == "1" && s[i + 1] == "3" && s[i + 2] == "#") {
            stringoutput += "m";
        }
        else if (s[i] == "1" && s[i + 1] == "4" && s[i + 2] == "#") {
            stringoutput += "n";
        }
        else if (s[i] == "1" && s[i + 1] == "5" && s[i + 2] == "#") {
            stringoutput += "o";
        }
        else if (s[i] == "1" && s[i + 1] == "6" && s[i + 2] == "#") {
            stringoutput += "p";
        }
        else if (s[i] == "1" && s[i + 1] == "7" && s[i + 2] == "#") {
            stringoutput += "q";
        }
        else if (s[i] == "1" && s[i + 1] == "8" && s[i + 2] == "#") {
            stringoutput += "r";
        }
        else if (s[i] == "1" && s[i + 1] == "9" && s[i + 2] == "#") {
            stringoutput += "s";
        }
        else if (s[i] == "2" && s[i + 1] == "0" && s[i + 2] == "#") {
            stringoutput += "t";
        }
        else if (s[i] == "2" && s[i + 1] == "1" && s[i + 2] == "#") {
            stringoutput += "u";
        }
        else if (s[i] == "2" && s[i + 1] == "2" && s[i + 2] == "#") {
            stringoutput += "v";
        }
        else if (s[i] == "2" && s[i + 1] == "3" && s[i + 2] == "#") {
            stringoutput += "w";
        }
        else if (s[i] == "2" && s[i + 1] == "4" && s[i + 2] == "#") {
            stringoutput += "x";
        }
        else if (s[i] == "2" && s[i + 1] == "5" && s[i + 2] == "#") {
            stringoutput += "y";
        }
        else if (s[i] == "2" && s[i + 1] == "6" && s[i + 2] == "#") {
            stringoutput += "z";
        }
        else {
            stringoutput += "";
        }
    }
    return stringoutput;
}
console.log(freqAlphabets("1326#"));
