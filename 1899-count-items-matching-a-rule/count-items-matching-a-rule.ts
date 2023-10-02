function countMatches(items: string[][], ruleKey: string, ruleValue: string): number {
    let counter = 0
    for (let i = 0;i<items.length;i++){
        let key
        if (ruleKey === 'type')
            key = items[i][0]
        else if(ruleKey==='color')
            key = items[i][1]
        else
            key = items[i][2]
        if (key === ruleValue)
            counter++
    }
    return counter
};