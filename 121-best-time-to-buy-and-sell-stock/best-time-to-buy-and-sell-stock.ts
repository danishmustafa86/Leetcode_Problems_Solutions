// function maxProfit(prices: number[]): number {
//     let maxprofit:number=0
//         for(let i:number=0;i<prices.length;i++){
//             for(let j:number=i+1;j<prices.length;j++){
//             if(prices[i]<prices[j])  {  
//                 let profit=prices[j]-prices[i]
//                 if(profit>maxprofit){
//                     maxprofit =profit
//                 }
//                 }
                
//             }
//     }

//     return maxprofit
// }

// function maxProfit(prices: number[]): number {
//     let maxProfit: number = 0;

//     for (let i: number = 0; i < prices.length; i++) {
//         for (let j: number = i + 1; j < prices.length; j++) {
//             if (prices[i] < prices[j]) {
//                 let profit = prices[j] - prices[i];
//                 if (profit > maxProfit) {
//                     maxProfit = profit; // Update the maximum profit if selling on this day yields a higher profit
//                 }
//             }
//         }
//     }

//     return maxProfit;
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
