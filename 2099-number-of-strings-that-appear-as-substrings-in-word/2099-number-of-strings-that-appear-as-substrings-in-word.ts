function numOfStrings(patterns: string[] = ["a", "abc", "bc", "d"], word: string = "abc"): number {
    let num1: number = 0;
    for (let j = 0; j < patterns.length; j++) {
        if (word.includes(patterns[j])) {
            num1++
        }

    }
    return num1;
}