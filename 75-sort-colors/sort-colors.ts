/**
 Do not return anything, modify nums in-place instead.
 */
// function sortColors(nums: number[]): void {

function sortColors(unsortedArray:number[]) {
    let sortedArray = [];
    let current;
    for (let i = 0; i < unsortedArray.length; i++) {
        current = unsortedArray[i]
        for (let j = i + 1; j < unsortedArray.length; j++) {

            if (unsortedArray[j] < current) {
                current = unsortedArray[j];
                unsortedArray[j] = unsortedArray[i];
                unsortedArray[i] = current;
            }

        }
        sortedArray.push(current);

    }

    return sortedArray
}

// };