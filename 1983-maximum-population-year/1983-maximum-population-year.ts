function maximumPopulation(logs: number[][]): number {
    let maxPop = -1, targetYear = -1;
    const popByYear = Array(100).fill(0);

    // mark the interval start and end points on the space 
    logs.forEach(([start, end]) => {
        const startNormalized = start - 1950;
        const endNormalized = end - 1950;
        popByYear[startNormalized] ??= 0;
        popByYear[startNormalized]++;

        popByYear[endNormalized] ??= 0;
        popByYear[endNormalized]--;
    });

    // 2. Assign values to all the points between intervals, which are currently empty
    for (let i = 1; i < popByYear.length; i++) {
        popByYear[i] += popByYear[i - 1];
    }

    // 3. sweep through the entire space and find the target year 
    popByYear.forEach((pop, yearNormalized) => {
        if (pop > maxPop) {
            maxPop = pop;
            targetYear = yearNormalized + 1950;
        } else if (pop === maxPop) {
            targetYear = Math.min(yearNormalized + 1950, targetYear);
        }
    });

    return targetYear;
};