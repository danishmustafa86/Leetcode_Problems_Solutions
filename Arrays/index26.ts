function pusOne(digits: number[]):number[] {
    let numarray: number[] = []
    let num1: string = ""
    let str: string = ""
    for (let i = 0; i < digits.length; i++) {
        let e = digits[i];
        num1 = e.toString()
        str = str.concat(num1)
    }
    let num2: number = parseInt(str)
    num2 = num2 + 1
    const numbsAsString: string = num2.toString();
    for (let j = 0; j < numbsAsString.length; j++) {
        const e = parseInt(numbsAsString[j],10);
        numarray.push(e)
    }

    return numarray
};
console.log(pusOne([2,3,56,4,1,5,4,0,8,0,0,7,3,1,5,6,0,0]));
