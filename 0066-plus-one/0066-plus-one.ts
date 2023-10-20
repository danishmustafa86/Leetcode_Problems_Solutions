// function plusOne(digits: number[]): number[] {
//     let numarray: number[] = [];
//     let num1: string = "";
//     let str: string = "";
    
//     for (let i = 0; i < digits.length; i++) {
//         let e = digits[i];
//         num1 = e.toString();
//         str = str.concat(num1);
//     }
    
//     let num2: number = parseInt(str);
//     num2 = num2 + 1;
    
//     const numbsAsString: string = num2.toString();
    
//     for (let j = 0; j < numbsAsString.length; j++) {
//         const e = parseInt(numbsAsString[j], 10); // Add the radix argument
//         numarray.push(e);
//     }

//     return numarray;
// }

// console.log(plusOne([1, 2, 3, 4]));

function plusOne(digits: number[]): number[] {
    for (let i = digits.length - 1; i >= 0; i--) {
        if (digits[i] === 9) {
            digits[i] = 0;
        } else {
            digits[i]++;
            return digits;
        }
    }
    return [1, ...digits];
};