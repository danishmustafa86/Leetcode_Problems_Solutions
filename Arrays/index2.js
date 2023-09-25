// You are given an m x n integer grid accounts where accounts[i][j] is the amount of 
// money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest 
// customer has.A customer's wealth is the amount of money they have in all their bank accounts. 
// The richest customer is the customer that has the maximum wealth.
// function maximumWealth(accounts: number[][]): number {
//     let maxWealth = 0;
//     for (let i = 0; i < accounts.length; i++) {
//         let currentCustomerWealth = 0;
//         for (let j = 0; j < accounts.length; j++) {
//             currentCustomerWealth += accounts[i][j];
//         }
//         maxWealth = Math.max(maxWealth, currentCustomerWealth);
//     }
//     return maxWealth;
// }
// // Example usage:
// const accounts: number[][] = [
//     [1, 2, 3],
//     [3, 2, 1],
//     [5, 4, 1]
// ];
// const richestCustomerWealth = maximumWealth(accounts);
// console.log(richestCustomerWealth); // This will output the richest customer's wealth
function wealth(accounts) {
    var maxwealth = 0;
    for (var i = 0; i < accounts.length; i++) {
        var accountsmoney = 0;
        for (var j = 0; j < accounts.length; j++) {
            accountsmoney = accountsmoney + accounts[i][j];
        }
        maxwealth = Math.max(maxwealth, accountsmoney);
    }
    return maxwealth;
}
var acounts = [
    [1, 2, 3, 4],
    [1, 35, 3, 7],
    [3, 4, 6]
];
var richestperson = wealth(acounts);
console.log(richestperson);
