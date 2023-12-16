function findContentChildren(g: number[], s: number[]): number {
    g.sort((a, b) => a - b);
    s.sort((a, b) => a - b);

    let contentChildren = 0;
    let cookieIndex = 0;

    for (let i = 0; i < g.length; i++) {
        while (cookieIndex < s.length && s[cookieIndex] < g[i]) {
            cookieIndex++;
        }

        if (cookieIndex < s.length) {
            contentChildren++;
            cookieIndex++;
        } else {
            break; // No more cookies available
        }
    }

    return contentChildren;
}

// Example usage:
const result = findContentChildren(
    [383, 384, 347, /*...*/],
    [494, 324, 293, /*...*/]
);

console.log(result); // Output: The maximum number of content children
