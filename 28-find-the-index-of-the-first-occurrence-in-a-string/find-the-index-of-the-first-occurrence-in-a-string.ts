
function strStr(haystack = "mississippi", needle = "issip"): number {
    for (let i = 0; i <= haystack.length - needle.length; i++) {
        if (haystack.substring(i, i+needle.length) == needle) {
            return i
        }
    }
    return -1
}
console.log(strStr());