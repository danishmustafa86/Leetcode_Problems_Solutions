function plusOne(digits) {
    var numarray = [];
    var num1 = "";
    var str = "";
    for (var i = 0; i < digits.length; i++) {
        var e = digits[i];
        num1 = e.toString();
        str = str.concat(num1);
    }
    var num2 = parseInt(str);
    num2 = num2 + 1;
    var numbsAsString = num2.toString();
    for (var j = 0; j < numbsAsString.length; j++) {
        var e = parseInt(numbsAsString[j], 10);
        numarray.push(e);
    }
    return numarray;
}
;
console.log(plusOne([2, 3, 56, 4, 1, 5, 4, 0, 8, 0, 0, 7, 3, 1, 5, 6, 0, 0]));
