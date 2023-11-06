function strStr(haystack = "mississippi", needle = "issip"): number {
    let num1: number = -1;

    if (needle === "") {
        return 0; // Handle the case where the needle is an empty string.
    }

    for (let i = 0; i < haystack.length; i++) {
        if (haystack[i] === needle[0]) {
            let match = true;
            for (let j = 0; j < needle.length; j++) {
                if (i + j >= haystack.length || haystack[i + j] !== needle[j]) {
                    match = false;
                    break;
                }
            }
            if (match) {
                num1 = i;
                break;
            }
        }
    }

    return num1;
}

console.log(strStr());
