function restoreString(s: string, indices: number[]): string {
    const shuffled: string[] = [];

    for (let i = 0; i < s.length; i++) {
        shuffled[indices[i]] = s[i];
    }

    return shuffled.join('')
}