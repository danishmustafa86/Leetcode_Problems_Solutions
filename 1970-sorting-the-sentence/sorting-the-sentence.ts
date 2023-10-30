function sortSentence(s: string): string {
    let arr:string[] = [];
    let strArr:string[] = s.split(' ')
    for(let i of strArr) {
        let index= parseInt(i.charAt(i.length-1))-1
        arr[index] = i.slice(0,i.length-1)
    };
    return arr.join(' ')
 };
console.log(sortSentence("how2 are3 you1"));