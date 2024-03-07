// function reverse(x: number) {
//     let st = x.toString();
//     st=st.split("").reverse().join("")
//     console.log(" my string is",st)
//     for(let i=0;i<st.length;i++){
//         if(st[i]== "-" ||st[i]== "+" || st[i]== "*" ||st[i]== "/" ||st[i]== "," ){
//         let newStr: string = st.slice(0, i) + st.slice(i + 1);
//           st=st[i]+st
//     // console.log(" my string is",newStr)

//         }
//     }
//     // let std=+st
//     return st
// };





function reverse(x: number): number {
    const isNegative = x < 0;
    let absX = Math.abs(x);
    let reversedStr = absX.toString().split("").reverse().join("");
    let reversedInt = +reversedStr;

    if (reversedInt > 2**31 - 1) {
        return 0;
    }

    return isNegative ? -reversedInt : reversedInt;
}


// function reverse(x: number) {
//     let st = x.toString();
//     st = st.split("").reverse().join("");
//     console.log("my string is", st);
//     for (let i = 0; i < st.length; i++) {
//         if (st[i] == "-" || st[i] == "+" || st[i] == "*" || st[i] == "/" || st[i] == ",") {
//             let newStr: string = st.slice(0, i) + st.slice(i + 1);
//             st = newStr;
//         }
//     }
//     let std = +st;
//     return st;
// }
