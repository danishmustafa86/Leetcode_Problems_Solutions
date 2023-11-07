function isLongPressedName(name: string, typed: string): boolean {
    if (name === typed) {
        return true;
    }

    let nameIndex = 0;
    for (let i = 0; i < typed.length; i++) {
        if (name[nameIndex] === typed[i]) {
            nameIndex++;
        } else if (i === 0 || typed[i] !== typed[i - 1]) {
            return false;
        }
    }

    return nameIndex === name.length;
}

// Example usage:
console.log(isLongPressedName("alex", "aaleex")); // Output: true
