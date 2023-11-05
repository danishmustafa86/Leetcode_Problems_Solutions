function reverseWords(s: string): string {
    let reversedSentence: string = ""
    const word = s.split(" ");
    for (let i = 0; i < word.length; i++) {
        const e = word[i];
        reversedSentence += e.split("").reverse().join("")
        if (i < word.length - 1) {
            reversedSentence += " "
        }

    }
    return reversedSentence
}