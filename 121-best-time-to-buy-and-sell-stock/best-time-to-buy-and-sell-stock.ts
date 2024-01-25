// function maxProfit(prices: number[]): number {
//     let arr:number[]=[]
//         for(let i:number=0;i<prices.length;i++){
            
//             if(prices[i]<prices[i+1])  {  
//                 for(let j:number=i+1;j<prices.length;j++){
//                     arr.push(prices[j]-prices[i])
//     }
//                 return Math.max(...arr);
//             }
//     }

//     return 0
// }







function maxProfit(prices: number[]): number {
    let maxProfit: number = 0;
    let minPrice: number = Infinity;

    for (let i: number = 0; i < prices.length; i++) {
        if (prices[i] < minPrice) {
            minPrice = prices[i]; // Update the minimum price seen so far
        } else if (prices[i] - minPrice > maxProfit) {
            maxProfit = prices[i] - minPrice; // Update the maximum profit if selling on this day yields a higher profit
        }
    }

    return maxProfit;
}
