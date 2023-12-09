// function romanToInt(s: string): number {
//     let n:number=0
//     for (let i:number = 0; i < s.length; i++) {
//         if (s[i]=="I"&&s[i+1]!="V"&&s[i+1]!="X")n+=1 
//        else if (s[i]=="I"&&s[i+1]=="V") n+=4
//       else  if (s[i]=="I"&&s[i+1]=="X") n+=9
//       else  if (s[i]=="V"&&s[i-1]!="I") n+=5; 
//       else  if (s[i]=="X"&&s[i-1]!="I") n+=10; 
//       else  if (s[i]=="L"&&s[i-1]!="X") n+=50; 
//       else  if (s[i]=="C"&&s[i-1]!="X") n+=100; 
//       else  if (s[i]=="X"&&s[i+1]=="L") n+=40; 
//       else  if (s[i]=="X"&&s[i+1]=="C") n+=90; 
//       else  if (s[i]=="D"&&s[i-1]!="C") n+=500; 
//       else  if (s[i]=="M"&&s[i-1]!="C") n+=1000; 
//       else  if (s[i]=="C"&&s[i+1]=="D") n+=400; 
//       else  if (s[i]=="C"&&s[i+1]=="M") n+=900; 
            
        
//     }
//     return n
// };


function romanToInt(s: string): number {
    let n: number = 0;

    for (let i: number = 0; i < s.length; i++) {
        if (s[i] == "I") {
            if (s[i + 1] == "V" || s[i + 1] == "X") {
                n -= 1;
            } else {
                n += 1;
            }
        } else if (s[i] == "V") {
            n += 5;
        } else if (s[i] == "X") {
            if (s[i + 1] == "L" || s[i + 1] == "C") {
                n -= 10;
            } else {
                n += 10;
            }
        } else if (s[i] == "L") {
            n += 50;
        } else if (s[i] == "C") {
            if (s[i + 1] == "D" || s[i + 1] == "M") {
                n -= 100;
            } else {
                n += 100;
            }
        } else if (s[i] == "D") {
            n += 500;
        } else if (s[i] == "M") {
            n += 1000;
        }
    }

    return n;
}

// // Examples
// console.log(romanToInt("III"));      // Output: 3
// console.log(romanToInt("LVIII"));    // Output: 58
// console.log(romanToInt("MCMXCIV"));  // Output: 1994
