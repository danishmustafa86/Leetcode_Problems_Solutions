function mySqrt(x: number): number {
 if (x == 0) {
return 0
//         throw new Error("Cannot find the square root of a negative number");
    }

    // Initial guess for the square root
    let guess = x / 2;

    // Iterate using the Newton-Raphson method
    for (let i = 0; i < 100; i++) {
        guess = 0.5 * (guess + x / guess);
    }
let num:number=Math.floor(guess)
    return num;
//     if(x<0){
// throw new Error ("cannot find the square root of a nagative number")
//          }
//          let guess:number=x/2
//          for 
    };
