function maximumWealth(accounts: number[][]): number {
    let maxWealth = 0;

    for (let i = 0; i < accounts.length; i++) {
        let currentCustomerWealth = 0;
        for (let j = 0; j < accounts[i].length; j++) {
            currentCustomerWealth += accounts[i][j];
        }
        
        maxWealth = Math.max(maxWealth, currentCustomerWealth);
    }
    
    return maxWealth;
}

// .log(maximumWealth());

