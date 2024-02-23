// function canPlaceFlowers(flowerbed: number[], n: number): boolean {
//     // flowerbed = [0].concat(flowerbed);
//     flowerbed.unshift(0);
//     flowerbed.push(0)
//     for(let i=1;i<flowerbed.length-1;i++){
//         if(flowerbed[i-1]==0 && flowerbed[i]==0 && flowerbed[i+1]==0){
//             n=n-1
//             flowerbed[i]=1
//         }
//     }
//     return n<0
// };

function canPlaceFlowers(flowerbed: number[], n: number): boolean {
    flowerbed.unshift(0);
    flowerbed.push(0);
    for(let i = 1; i < flowerbed.length - 1; i++) {
        if(flowerbed[i - 1] === 0 && flowerbed[i] === 0 && flowerbed[i + 1] === 0) {
            n--;
            flowerbed[i] = 1; // Corrected line
        }
    }
    return n <= 0;
}
