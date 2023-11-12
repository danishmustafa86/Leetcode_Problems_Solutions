function strStr(haystack = "mississippi", needle = "issip"): number {
    if (needle === "") {
        return 0; // Handle the case where the needle is an empty string.
    }

    for (let i = 0; i <= haystack.length - needle.length; i++) {
        if (haystack.substring(i, i + needle.length) === needle) {
            return i;
        }
    }

    return -1; // Needle not found in haystack
}

console.log(strStr());
