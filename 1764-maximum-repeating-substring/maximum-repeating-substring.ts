function maxRepeating(sequence: string, word: string): number {
    let count: number = 0;
    let currentWord: string = word;

    while (sequence.includes(currentWord)) {
        count++;
        currentWord += word;
    }

    return count;
}